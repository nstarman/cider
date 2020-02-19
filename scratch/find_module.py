# -*- coding: utf-8 -*-

# ----------------------------------------------------------------------------
#
# TITLE   :
# AUTHOR  :
# PROJECT :
#
# ----------------------------------------------------------------------------

# Docstring
"""**DOCSTRING**.

description

Routing Listings
----------------

"""


###############################################################################
# IMPORTS

# GENERAL

# CUSTOM

# PROJECT-SPECIFIC


###############################################################################
# PARAMETERS


###############################################################################
# CODE
###############################################################################


###############################################################################
# Command Line
###############################################################################

from modulefinder import ModuleFinder

print(dir(ModuleFinder))

finder = ModuleFinder()
finder.run_script('bacon.py')

print('Loaded modules:')
for name, mod in finder.modules.items():
    print('%s: ' % name, end='')
    print(','.join(list(mod.globalnames.keys())[:3]))

print('-'*50)
print('Modules not imported:')
print('\n'.join(finder.badmodules.keys()))

###############################################################################
# END
