from .. import merge_sort
from random import shuffle
import pytest


def test_alive():
    """ Does our test file even run
    """
    pass


def test_merge_sort_exists():
    """ can we see the basic function
    """
    assert merge_sort


@pytest.fixture
def empty_list():
    return []


def test_merge_sort_shuffled_list_gets_sorted():
    """ Take a random ordered list, does our algo sort correctly
    """
    expected = [num for num in range(20)]
    unsorted = expected[:]
    shuffle(unsorted)
    print(unsorted)
    now_sorted = merge_sort(unsorted)
    print(now_sorted)
    assert expected == now_sorted


def test_merge_sort_already_sorted():
    """ Does our algo handle when input is already sorted
    """
    expected = [num for num in range(20)]
    now_sorted = merge_sort(expected)
    assert expected == now_sorted


def test_merge_sort_list_of_duplicates():
    """ Does our algo work if there are duplicates.
    """
    unsorted = [4, 4, 5, 3, 2, 3, 4, 3, 4, 5]
    expected = [2, 3, 3, 3, 4, 4, 4, 4, 5, 5]
    now_sorted = merge_sort(unsorted)
    assert expected == now_sorted

