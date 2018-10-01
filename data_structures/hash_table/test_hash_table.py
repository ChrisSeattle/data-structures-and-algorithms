from .hash_table import HashTable
from .binary_tree import BinaryTree
import pytest


def test_alive():
    """ Does our test file even run
    """
    pass


def test_hash_table_exists():
    """ can we see the class
    """
    assert HashTable


def test_binary_get_exists():
    """ can we see the class
    """
    assert BinaryTree.get


@pytest.fixture
def empty_hash():
    return HashTable()


@pytest.fixture
def given_bt():
    input = [20, 18, 12, 19, 11, 14, 40, 31, 22, 33]
    b = BinaryTree(input)
    return b

@pytest.fixture
def bt_pairs():
    input = {
        20: 'twenty', 18: 'eighteen', 12: 'twelve', 19: 'nineteen',
        11: 'eleven', 40: 'forty', 31: 'thirtyone', 22: 'twentytwo'
    }
    p = BinaryTree(input)
    return p

@pytest.fixture
def collision():
    value = 'tis sit its sit'
    h = HashTable()
    h.set(value)
    return h


def test_bt_get_returns_expected(given_bt):
    """
    """
    actual = given_bt.get(11)
    expected = 11
    assert expected == actual


def test_bt_get_returns_false_on_not_present(given_bt):
    """
    """
    actual = given_bt.get(100)
    expected = False
    assert expected == actual


def test_bt_get_returns_expected_pairs(bt_pairs):
    """
    """
    actual = bt_pairs.get(11)
    expected = 'eleven'
    assert expected == actual
    actual = bt_pairs.get(22)
    expected = 'twentytwo'
    assert expected == actual






