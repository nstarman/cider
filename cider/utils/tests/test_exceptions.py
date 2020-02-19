# -*- coding: utf-8 -*-

"""Test Citation Decorator."""

# __all__ = [
#     ""
# ]


###############################################################################
# IMPORTS

# GENERAL

import warnings
import pytest


###############################################################################
# CODE
###############################################################################


def test_DocStringFormatWarning():
    """Test DocStringFormatWarning."""
    from ..exceptions import DocStringFormatWarning

    with pytest.warns(DocStringFormatWarning):
        warnings.warn("DocStringFormatWarning", DocStringFormatWarning)


# /def


# --------------------------------------------------------------------------


###############################################################################
# END
