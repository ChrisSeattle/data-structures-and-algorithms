from .. import radix_sort
from random import shuffle
import pytest


def test_alive():
    """ Does our test file even run
    """
    pass


def test_radix_sort_name_exists():
    """ can we see the basic function
    """
    assert radix_sort


@pytest.fixture
def empty_list():
    return []


def test_sort_on_shuffled_list_radix_sort():
    """ Take a random ordered list, does our algo sort correctly
    """
    # expected = [num for num in range(20)]
    expected = [0, 7, 13, 16, 21, 42, 169, 301, 404, 423, 8374]
    unsorted = expected[:]
    shuffle(unsorted)
    print(unsorted)
    now_sorted = radix_sort(unsorted)
    print(now_sorted)
    assert expected == now_sorted


def test_already_sorted_radix_sort():
    """ Does our algo handle when input is already sorted
    """
    expected = [num for num in range(20)]
    now_sorted = radix_sort(expected)
    assert expected == now_sorted


def test_list_of_duplicates_radix_sort():
    """ Does our algo work if there are duplicates.
    """
    unsorted = [4, 4, 5, 3, 2, 3, 4, 3, 4, 5]
    expected = [2, 3, 3, 3, 4, 4, 4, 4, 5, 5]
    now_sorted = radix_sort(unsorted)
    assert expected == now_sorted
