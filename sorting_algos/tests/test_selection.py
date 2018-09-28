from .. import selection_sort
from random import shuffle
import pytest


def test_alive():
    """ Does our test file even run
    """
    pass


def test_function_name_exists():
    """ can we see the basic function
    """
    assert selection_sort


@pytest.fixture
def empty_list():
    return []


def test_shuffled_list_gets_sorted():
    """ Take a random ordered list, does our algo sort correctly
    """
    expected = [num for num in range(20)]
    unsorted = expected[:]
    shuffle(unsorted)
    now_sorted = selection_sort(unsorted)
    assert expected == now_sorted


def test_sorts_already_sorted():
    """ Does our algo handle when input is already sorted
    """
    expected = [num for num in range(20)]
    now_sorted = selection_sort(expected)
    assert expected == now_sorted


def test_sorts_list_of_duplicates():
    """ Does our algo work if there are duplicates.
    """
    unsorted = [4, 4, 5, 3, 2, 3, 4, 3, 4, 5]
    expected = [2, 3, 3, 3, 4, 4, 4, 4, 5, 5]
    now_sorted = selection_sort(unsorted)
    assert expected == now_sorted


def test_sort_validates_expected_input():
    """ If inappropriate input given, does it raise TypeError
    """
    with pytest.raises(TypeError):
        selection_sort('hello world')
