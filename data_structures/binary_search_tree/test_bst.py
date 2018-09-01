from .bst import Node, BinaryTree
import pytest


def test_alive():
    """ Does our test file even run
    """
    pass


@pytest.fixture
def insert_list():
    a = BinaryTree()
    a.insert(42)
    a.insert(13)
    a.insert(7)
    return a


@pytest.fixture
def given_list():
    input = [20, 18, 12, 19, 11, 14, 40, 31, 22, 33]
    b = BinaryTree(input)
    return b


def test_node_exists():
    """ can we see the basic function
    """
    assert Node


def test_node_pointing_properties():
    """ Does the Node have the properties we need for BinaryTree
    """
    a = Node(42)
    assert a.left
    assert a.right


def test_node_str_and_repr():
    """ Does this node have the str and repr we expect
    """
    a_left = Node(7, data='payload left')
    a_right = Node(42, data='payload right')
    a = Node(13, data='payload a', left=a_left, right=a_right)
    string_a = str(a)
    repr_a = repr(a)
    assert string_a == repr_a


def test_binarytree_exists():
    """ can we see the basic function
    """
    assert BinaryTree


def test_binarytree_instantiate_null():
    """ Can we instantiate with no intial values
    """
    b = BinaryTree()
    assert isinstance(b, BinaryTree)


def test_binarytree_instantiate_single_value():
    """ Can we instantiate with no intial values
    """
    b = BinaryTree(42)
    assert isinstance(b, BinaryTree)


def test_binarytree_instantiate_list():
    """ Can we instantiate with intial list
    """
    input = [13, 42, 7]
    c = BinaryTree(input)
    assert isinstance(c, BinaryTree)


def test_binarytree_instantiate_tuple():
    """ Can we instantiate with intial list
    """
    input = (13, 42, 7)
    d = BinaryTree(input)
    assert isinstance(d, BinaryTree)


def test_binarytree_instantiate_error_list():
    """ The following list should cause an error on the third value
    """
    input = [42, 13, 13]
    f = BinaryTree(input)
    expected = ''
    assert f == expected


def test_binarytree_insert_error_list():
    """ The following list should cause an error on the third value
    """
    input = [42, 13, 13]
    f = BinaryTree(input)
    expected = ''
    assert f == expected


def test_binarytree_insert_exists(given_list):
    """ Can we see the insert method
    """
    assert BinaryTree.insert


def test_binarytree_in_order(given_list):
    """ can we see in_order method
    """
    assert BinaryTree.in_order


def test_binarytree_pre_order(given_list):
    """ can we see pre_order method
    """
    assert BinaryTree.pre_order


def test_binarytree_post_order(given_list):
    """ can we see post_order method
    """
    assert BinaryTree.post_order




def test_function_name_results_are_a_certain_way(empty_list):
    """ docstring on what we are checking
    """
    expected = 44
    actual = empty_list.method(44)
    assert expected == actual

