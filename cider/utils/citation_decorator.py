# -*- coding: utf-8 -*-

"""Add citation information to functions.

The purpose of the provided decorator is to add relevant citation information
to functions copied from other package repositories. Alternatively, if
the docstrings are in the numpy-doc or numpy-napoleon style the citation
information may be added to the `References` section of the docstring.
However, using the decorator minimizes changes to the original function and
may therefore be preferable.

Routing Listings
----------------
citation_decorator

"""

# __all__ = [
#     ""
# ]


###############################################################################
# IMPORTS

# GENERAL

import functools

# CUSTOM

# PROJECT-SPECIFIC

from .doc_parse_tools import store


###############################################################################
# CODE
###############################################################################


def citation_decorator(
    function=None, citation=None, style=None, doc_style=None, add_to_doc=False
):
    """Add citation information to functions.

    The purpose of this decorator is to add relevant citation information
    to functions copied from other package repositories. This also merges all
    citation information from `References`, if the docstrings are in the
    numpy-doc or numpy-napoleon format.

    Parameters
    ----------
    function : types.FunctionType or None, optional
        the function to be decorated
        if None, then returns decorator to apply.
    citation : str, optional
        key-word only arguments
        sets the wrapper's default values.
    style: str, optional
        the citation style.
        used if the citation style cannot be auto-determined.
    doc_style : str or type, optional
        the docstring style.
        needed if the format cannot be auto-determined.
        determines the parser type to extract references.
    add_to_doc : bool, optional
        whether to add to docstring

    Returns
    -------
    wrapper : types.FunctionType
        wrapper for function
        does a few things
        includes the original function in a method `.__wrapped__`

    Raises
    ------
    DocStringFormatWarning
        if the format of the docstring cannot be determined.

    """
    if function is None:  # allowing for optional arguments
        return functools.partial(citation_decorator, citation=citation)

    @functools.wraps(function)
    def wrapper(*args, **kw):
        return function(*args, **kw)

    # /def

    # TODO parse the citations from reference
    # first determine the citation format
    # then get the references

    # TODO add to doc, if add_to_doc
    if add_to_doc:
        pass

    # TODO process citation into BibTex Format
    wrapper.__citation___ = citation  # store citation

    # store information related to citation
    wrapper.meta = {
        "citation": citation,
        "style": style,
        "doc_style": doc_style,
        "add_to_doc": add_to_doc,
    }

    return wrapper


# /def


###############################################################################
# END
