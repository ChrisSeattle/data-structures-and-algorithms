from .binary_tree import Node, Queue, BinaryTree
from .max_val import find_maximum_value
import pytest


def test_alive():
    """ Does our test file even run
    """
    pass


def test_find_maximum_value_exists():
    """ Can we see the function
    """
    assert find_maximum_value


@pytest.fixture
def empty_list():
    e = BinaryTree()
    return e


@pytest.fixture
def given_list():
    input = [20, 18, 12, 19, 11, 14, 40, 31, 22, 33]
    b = BinaryTree(input)
    return b

def test_we_get_expected_error_when_called_with_not_tree():
    """ find_maximum_value function should return informative
        error if it is called with non-BinaryTree inputs
    """
    with pytest.raises(TypeError):
        find_maximum_value('string')


def test_instantiate_tree_with_no_nodes(empty_list):
    """ Can we instantiate a BinaryTree with a list of inputs
    """
    assert isinstance(empty_list, BinaryTree)


def test_instantiate_tree_with_values(given_list):
    """ Can we instantiate a BinaryTree with a list of inputs
    """
    assert isinstance(given_list, BinaryTree)


def test_do_we_get_max_on_given_list(given_list):
    """ If we have a BinaryTree with values, do we find the max
    """
    expected = 40
    actual = find_maximum_value(given_list)
    assert expected == actual


def test_max_on_empty_tree(empty_list):
    """ Does our function handle when BT has no nodes
    """
    result = find_maximum_value(empty_list)
    assert result is None


def test_max_on_tree_with_negative_val_in_nodes():
    """ What if we have all negative values in the tree
    """
    input = [-10, -15, -7, -13, -42]
    neg_tree = BinaryTree(input)
    expected = -7
    actual = find_maximum_value(neg_tree)
    assert expected == actual


def test_can_make_binary_tree_with_new_tree_and_old_tree(given_list, capsys):
    """ We are going to create a new Binary Tree, set it's root left to an
        already established tree. Does this new tree accuratly inherit all
        of the children
    """
    new_tree = BinaryTree(40)
    new_tree.root.left = given_list.root
    expected = [40, 20, 18, 40, 12, 19, 31, 11, 14, 22, 33]
    new_tree.breadth_first()
    out, err = capsys.readouterr()
    actual = [int(i) for i in out.split('\n') if i != '']
    assert expected == actual


def test_max_on_tree_with_duplicate_values(given_list, capsys):
    """ Does our function have issues if it hits duplicates
        that qualify as the max value
    """
    new_tree = BinaryTree(40)
    new_tree.root.left = given_list.root
    expected = 40
    actual = find_maximum_value(given_list)
    assert expected == actual
