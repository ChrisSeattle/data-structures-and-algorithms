from .queue_with_stacks import queue_with_stacks
import pytest


def test_alive():
    pass


def test_function_name_exists():
    assert queue_with_stacks


def test_function_name_results_are_a_certain_way():
    expected = 44
    actual = function_name('input')
    assert expected == actual


@pytest.fixture
def empty_list():
    return LinkedList()


@pytest.fixture
def small_list():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    return ll


def test_linked_list_exists():
    assert LinkedList


def test_linked_list_results(small_list)
    #
    #
    pass

