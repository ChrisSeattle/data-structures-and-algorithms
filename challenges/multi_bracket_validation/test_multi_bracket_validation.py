from .multi_bracket_validation import multi_bracket_validation
# from .multi_bracket_validation import multi_bracket_validation
# from ... data_structures.stack.stack import Stack
import pytest


def test_alive():
    """ Does our test file even run
    """
    pass


def test_multi_bracket_validation_exists():
    """ can we see the basic function
    """
    assert multi_bracket_validation


def test_multi_bracket_validation_passes_easy():
    """ this input is easy to see it should pass
    """
    a = '(this[is some {input that} should] work)easy'
    assert multi_bracket_validation(a)


def test_multi_bracket_validation_passes_sibling_brackets():
    """ The validation should work if ther are sibling brackets
    """
    b = 'this (is [some] {input that} [should] also)()pass'
    assert multi_bracket_validation(b)


def test_multi_bracket_validation_false_for_overlapping():
    """ If the brackets overlap, we should get a False return
    """
    c = '(Oops[sometimes] [there {is] accidental} overlap)'
    assert multi_bracket_validation(c) is False


def test_multi_bracket_validation_false_for_unfinished():
    """ If we nested just fine, but forgot one, should return false
    """
    d = 'hey, (do not [forget] {we have} a (paranthesis) still'
    assert multi_bracket_validation(d) is False
