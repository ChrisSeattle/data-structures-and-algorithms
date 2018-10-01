from .bt import BinaryTree
from .tree_intersection import tree_intersection
import pytest


def test_alive():
    """ Does our test file even run
    """
    pass


def test_tree_intersection_name_exists():
    """ can we see the tree_intersection function
    """
    assert tree_intersection


@pytest.fixture
def empty():
    e = BinaryTree()
    return e


@pytest.fixture
def first_example():
    input = [150, 100, 250, 75, 160, 200, 350, 125, 175, 300, 500]
    a = BinaryTree(input)
    return a


@pytest.fixture
def second_example():
    input = [42, 100, 600, 15, 160, 200, 350, 125, 175, 4, 500]
    b = BinaryTree(input)
    return b


@pytest.fixture
def one_wb():
    input = [150, 100, 200, 141, 170]
    return BinaryTree(input)


@pytest.fixture
def two_wb():
    input = [142, 140, 160, 100, 141, 200, 12, 150]
    return BinaryTree(input)


def test_tree_intersection_on_whiteboard_example(one_wb, two_wb):
    """ docstring on what we are checking
    """
    expected = [200, 150, 141, 100]
    actual = tree_intersection(one_wb, two_wb)
    assert expected == actual


def test_tree_intersection_on_challenge_example(first_example, second_example):
    """ docstring on what we are checking
    """
    expected = [500, 350, 200, 175, 160, 125, 100]
    actual = tree_intersection(first_example, second_example)
    assert expected == actual
