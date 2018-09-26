from .hash_table import HashTable
import pytest


def test_alive():
    """ Does our test file even run
    """
    pass


def test_function_name_exists():
    """ can we see the basic function
    """
    assert repeated_word


def test_class_name_exists():
    """ can we see the class
    """
    assert HashTable


@pytest.fixture
def empty():
    return HashTable()


def test_repeated_word_no_repeats():
    """
    """
    string = 'It is possible to have no repeats'
    expected = None
    actual = repeated_word(string)
    assert expected == actual


def test_repeated_word_simple_repeat():
    """ no collisions before finding repeated word
    """
    string = 'the the'
    actual = repeated_word(string)
    expected = 'the'
    assert expected == actual


def test_repeated_words_ignores_case():
    """ It should ignore the case of the words
    """
    string = 'The the'
    actual = repeated_word(string)
    expected = 'the'
    assert expected == actual


def test_repeated_words_ignores_ending_punctuation():
    """ If a word has an ending punctuation, it should be ignored.
    """
    string = 'the the.'
    actual = repeated_word(string)
    expected = 'the'
    assert expected == actual


def test_repeated_words_ignores_non_word_characters():
    """
    """
    pass


def test_repeated_word_collision_repeat():
    """ docstring on what we are checking
    """
    string = 'tis sit its sit'
    expected = 'sit'
    actual = repeated_word(string)
    assert expected == actual
