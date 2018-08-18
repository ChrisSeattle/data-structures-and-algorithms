# from .this_directory import function_name, other_function
from .linked_list import LinkedList, Node
import pytest


def test_alive():
    pass


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


def test_create_instance_of_list():
    ll = LinkedList()
    assert isinstance(ll, LinkedList)


def test_default_property_head(empty_list):
    assert empty_list._length == 0


def test_linked_list_insert_exists():
    assert LinkedList.insert


def test_linked_list_insertion_successful():
    ll = LinkedList()
    assert ll.head is None
    ll.insert(25)
    assert ll.head.val == 25


def test_length_of_list_increases_on_insertion():
    ll = LinkedList()
    assert len(ll) == 0
    ll.insert(42)
    assert len(ll) == 1


def test_node_exists():
    assert Node


def test_node_str_return():
    input_a = [7, 13, 42]
    input_b = 42
    expected_a = str(input_a)
    expected_b = str(input_b)
    actual_a = str(Node(input_a))
    actual_b = str(Node(input_b))
    assert expected_a == actual_a
    assert expected_b == actual_b


def test_node_repr_return():
    input = [7, 13, 42]
    expected = f'<Node | Val: {input} | Next: None>'
    actual = Node(input)
    assert expected == actual



