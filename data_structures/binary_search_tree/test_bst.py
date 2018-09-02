from .bst import Node, BinaryTree
import pytest


def test_alive():
    """ Does our test file even run
    """
    pass


@pytest.fixture
def empty_list():
    e = BinaryTree()
    return e


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
    a_left = Node(7, data='pl left')
    a_right = Node(42, data='pl right')
    a = Node(13, data='pl a', left=a_left, right=a_right)
    assert a.left.val == 7
    assert a.right.val == 42


def test_node__repr():
    """ Does this node have the repr we expect
    """
    a_left = Node(7, data='pl left')
    a_right = Node(42, data='pl right')
    a = Node(13, data='pl a', left=a_left, right=a_right)
    repr_a = repr(a)
    expect_repr = '<Node | Val: 13 | Data: pl a | Left: 7 | Right: 42>'
    assert expect_repr == repr_a


def test_node_str():
    """ Does this node have the str we expect
    """
    a_left = Node(7, data='pl left')
    a_right = Node(42, data='pl right')
    a = Node(13, data='pl a', left=a_left, right=a_right)
    string_a = str(a)
    expect_string = '13'
    assert string_a == expect_string


def test_binarytree_exists():
    """ can we see BinaryTree class
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
    """ Can we instantiate with a list
    """
    input = [13, 42, 7]
    c = BinaryTree(input)
    assert isinstance(c, BinaryTree)


def test_instantiate_gets_correct_root_and_root_pointers():
    """ Does the root get set, and does it have the correct left and right
    """
    input = [13, 42, 7]
    c = BinaryTree(input)
    root_repr = repr(c.root)
    expected_root_repr = '<Node | Val: 13 | Data: None | Left: 7 | Right: 42>'
    assert root_repr == expected_root_repr


def test_binarytree_instantiate_tuple():
    """ Can we instantiate with a tuple
    """
    input = (13, 42, 7)
    d = BinaryTree(input)
    assert isinstance(d, BinaryTree)


def test_binarytree_str_as_expected():
    """ After instanting with a few items, does BinaryTree str look right.
    """
    input = (13, 42, 7)
    expected = 'BinaryTree | Root: 13'
    s = BinaryTree(input)
    actual = str(s)
    assert expected == actual


def test_binarytree_repr_as_expected():
    """ After instantiating with a list, does the BinaryTree repr look right
    """
    input = [13, 42, 7]
    expected = '<BinaryTree | Root: 13>'
    r = BinaryTree(input)
    actual = repr(r)
    assert expected == actual


def test_instantiate_six_nodes():
    """ Does it work to instantiate with 6 initial values
        So far we have only tried instantiating with 3 values
    """
    input = [13, 42, 7, 3, 9, 99]
    six = BinaryTree(input)
    assert isinstance(six, BinaryTree)


def test_binarytree_insert_exists(empty_list):
    """ Can we see the insert method
    """
    assert empty_list.insert(42)


def test_binarytree_insert_error_expected():
    """ The following list should cause an error on the third value
    """
    input = [42, 13]
    f = BinaryTree(input)
    with pytest.raises(ValueError) as err:
        f.insert(13)
    expected = 'Neither < or > for 13, 13'
    assert 'ValueError' in str(err.type)
    assert expected == str(err.value)


def test_binarytree_instantiate_given(given_list):
    """ Can we instantiate with intial list
    """
    assert isinstance(given_list, BinaryTree)


def test_binarytree_instantiate_error_list(capsys):
    """ The following list should cause an error on the third value
    """
    input = [42, 13, 13]
    with pytest.raises(ValueError) as err:
        BinaryTree(input)
    expected = 'Neither < or > for 13, 13'
    assert 'ValueError' in str(err.type)
    assert expected == str(err.value)


def test_binarytree_in_order_exists():
    """ can we see in_order method
        left, visit, right
    """
    assert BinaryTree.in_order


def test_binarytree_in_order_correct_on_given(given_list, capsys):
    """ can we see in_order method
        left, visit, right
    """
    expected = [11, 12, 14, 18, 19, 20, 22, 31, 33, 40]
    given_list.in_order()
    out, err = capsys.readouterr()
    actual = [int(i) for i in out.split('\n') if i != '']
    assert expected == actual


def test_binarytree_pre_order_exists():
    """ can we see in_order method
        visit, left, right
    """
    assert BinaryTree.pre_order


def test_binarytree_pre_order_on_given(given_list, capsys):
    """ can we see pre_order method
        visit, left, right
    """
    expected = [20, 18, 12, 11, 14, 19, 40, 31, 22, 33]
    given_list.pre_order()
    out, err = capsys.readouterr()
    actual = [int(i) for i in out.split('\n') if i != '']
    assert expected == actual


def test_binarytree_post_order_exists():
    """ can we see in_order method
        left, right, visit
    """
    assert BinaryTree.post_order


def test_binarytree_post_order_on_given(given_list, capsys):
    """ can we see post_order method
       left, right, visit
    """
    expected = [11, 14, 12, 19, 18, 22, 33, 31, 40, 20]
    given_list.post_order()
    out, err = capsys.readouterr()
    actual = [int(i) for i in out.split('\n') if i != '']
    assert expected == actual
