from .. import selection_sort
from random import shuffle
import pytest


def test_alive():
    """ Does our test file even run
    """
    pass


def test_selection_sort_name_exists():
    """ can we see the basic function
    """
    assert selection_sort


@pytest.fixture
def empty_list():
    return []


def test_sort_on_shuffled_list_selection_sort():
    """ Take a random ordered list, does our algo sort correctly
    """
    expected = [num for num in range(20)]
    unsorted = expected[:]
    shuffle(unsorted)
    print(unsorted)
    now_sorted = selection_sort(unsorted)
    print(now_sorted)
    assert expected == now_sorted


def test_already_sorted_selection_sort():
    """ Does our algo handle when input is already sorted
    """
    expected = [num for num in range(20)]
    now_sorted = selection_sort(expected)
    assert expected == now_sorted


def test_list_of_duplicates_selection_sort():
    """ Does our algo work if there are duplicates.
    """
    unsorted = [4, 4, 5, 3, 2, 3, 4, 3, 4, 5]
    expected = [2, 3, 3, 3, 4, 4, 4, 4, 5, 5]
    now_sorted = selection_sort(unsorted)
    assert expected == now_sorted


def test_validates_expected_input_selection_sort():
    """ If inappropriate input given, does it raise TypeError
    """
    with pytest.raises(TypeError):
        selection_sort('hello world')
