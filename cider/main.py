import sys
import dis
import importlib
from modulefinder import ModuleFinder
import click
import stdlib_list

# Load value of __citation__, __cite__, __bibtex__ from reading a module's code
# From https://stackoverflow.com/a/51090571/10195320
def load_citation_info(name, mod):
    """Requires that the globals are set from a literal constant value"""
    if (
        not "__citation__" in mod.globalnames
        and not "__cite__" in mod.globalnames
        and not "__bibtex__" in mod.globalnames
    ):
        return -1
    # Try loading from reading the code and finding literal constants
    try:
        instructions = dis.get_instructions(mod.__code__)
    except:
        return -1
    for instr in instructions:
        if instr.opname == "LOAD_CONST":
            nxtop = next(instructions, None)
            if nxtop.opname == "STORE_NAME" and nxtop.argval == "__citation__":
                return instr.argval
            elif nxtop.opname == "STORE_NAME" and nxtop.argval == "__cite__":
                return instr.argval
            elif nxtop.opname == "STORE_NAME" and nxtop.argval == "__bibtex__":
                return instr.argval
        # If reading literals doesn't work, code has the attribute,
        # but not a literal, so we need to load
        loaded_mod = importlib.import_module(name)
        if "__citation__" in mod.globalnames:
            return loaded_mod.__citation__
        elif "__cite__" in mod.globalnames:
            return loaded_mod.__cite__
        if "__bibtex__" in mod.globalnames:
            return loaded_mod.__bibtex__
    return -1


def format_output(cite_info):
    for key in cite_info:
        print(key, cite_info[key])
    return None


@click.command()
@click.argument("path")
@click.option(
    "-d",
    "--depth",
    default=2,
    help="""How deep in a package to look for citation info 
(e.g., scipy.spatial is depth=2')""",
)
def run(path, depth):
    std_lib_modules = stdlib_list.stdlib_list(
        "{}.{}".format(sys.version_info.major, sys.version_info.minor)
    )
    finder = ModuleFinder()
    finder.run_script(path)
    cite_info = {}
    for name, mod in finder.modules.items():
        if len(name.split(".")) > depth:
            continue
        if name in std_lib_modules:
            continue
        if name.startswith("_"):
            continue
        this_cite_info = load_citation_info(name, mod)
        if not this_cite_info == -1:
            cite_info[name] = this_cite_info
    format_output(cite_info)
    return None


if __name__ == "__main__":
    run()
