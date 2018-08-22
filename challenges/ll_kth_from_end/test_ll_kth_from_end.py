from .ll_kth_from_end import LinkedList, Node
# from .node_class import LinkedList, Node
import pytest


def test_alive():
    pass


@pytest.fixture
def empty_list():
    return LinkedList([])


@pytest.fixture
def small_list():
    ll = LinkedList([])
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    return ll


def test_ll_kth_from_end_exists():
    assert LinkedList.ll_kth_from_end


def test_ll_kth_from_end_item_not_in_list(small_list):
    expected = 'Exemption'
    actual = ll_kth_from_the_end(5)
    assert expected == actual


def test_ll_kth_from_end_last_num(small_list):
    expected = 4
    actual = ll_kth_from_the_end(0)
    assert expected == actual


def test_ll_kth_from_end_item_first_num(small_list):
    expected = 1
    actual = ll_kth_from_the_end(3)
    assert expected == actual


def test_ll_kth_from_end_item_middle_num(small_list):
    expected = 3
    actual = ll_kth_from_the_end(1)
    assert expected == actual


def test_ll_kth_from_end_empty_list(empty_list):
    expexted = 'Exemption'
    actual = ll_kth_from_the_end(5)
    assert expexted == actual


# def test_function_name_results_are_a_certain_way():
#     expected = 44
#     actual = function_name('input')
#     assert expected == actual


# @pytest.fixture
# def empty_list():
#     return LinkedList()


# @pytest.fixture
# def small_list():
#     ll = LinkedList()
#     ll.insert(1)
#     ll.insert(2)
#     ll.insert(3)
#     ll.insert(4)
#     return ll


# def test_linked_list_exists():
#     assert LinkedList


# def test_linked_list_results(small_list)
#     #
#     #
#     pass

