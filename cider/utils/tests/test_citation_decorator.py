# -*- coding: utf-8 -*-

"""Test Citation Decorator."""

# __all__ = [
#     ""
# ]


###############################################################################
# CODE
###############################################################################


def test_decorator_base():
    """Test Decorator Basic Function."""
    from ..citation_decorator import citation_decorator

    citation = 'test citation'

    @citation_decorator(citation=citation)
    def test_function():
        pass

    assert test_function.__citation__ == citation


# /def


# --------------------------------------------------------------------------

def test_style_arg():
    """Test Decorator `style` Argument."""
    pass


# /def


# --------------------------------------------------------------------------


def test_doc_style_arg():
    """Test Decorator `doc_style` Argument."""
    pass


# /def


# --------------------------------------------------------------------------


def test_add_to_doc_arg():
    """Test Decorator `add_to_doc` Argument."""
    pass


# /def


###############################################################################
# END
