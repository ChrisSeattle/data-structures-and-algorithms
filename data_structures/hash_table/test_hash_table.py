from .hash_table import HashTable
from .binary_tree import BinaryTree, Node
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
def ht_nums():
    inp = {
        'twenty': 20, 'eighteen': 18, 'twelve': 12, 'nineteen': 19, 'eleven':
        11, 'forty': 40, 'thirtyone': 31, 'twentytwo': 22
    }
    ht = HashTable()
    for (word, num) in inp.items():
        ht.set(word, num)
    return ht

@pytest.fixture
def collision():
    value = 'tis sit its sit'
    h = HashTable()
    for word in value.split():
        h.set(word)
    return h


def test_bt_get_returns_expected(given_bt):
    """ Does the Binary Tree get method retrieve the expected result
    """
    actual = given_bt.get(11)
    expected = 11
    assert expected == actual


def test_bt_get_returns_false_on_not_present(given_bt):
    """ If the value is not in the Binary Tree, we should get a false
    """
    actual = given_bt.get(100)
    expected = False
    assert expected == actual


def test_bt_get_returns_expected_pairs(bt_pairs):
    """ Does the Binary Tree get retrieve the actual data for the value
    """
    actual = bt_pairs.get(11)
    expected = 'eleven'
    assert expected == actual
    actual = bt_pairs.get(22)
    expected = 'twentytwo'
    assert expected == actual


def test_bt_insert_node_works(bt_pairs):
    """
    """
    val = 42
    data = 'fourty-two'
    n = Node(val, data)
    success = bt_pairs.insert_node(n)
    assert success is True
    assert data == bt_pairs.get(val)


def test_bt_delete_works(bt_pairs):
    """ Remove the key-value pair when delete is called
    """
    expected = 'eleven'
    actual = bt_pairs.delete(11)
    assert expected == actual


def test_bt_delete_false_on_not_present_node(bt_pairs):
    """ If the value is not present, do we get the expected false response
    """
    assert bt_pairs.delete(42) is False


def test_ht_set_works():
    """ Can we set a new input to the hash table?
    """
    ht = HashTable()
    ht.set('fourty-two', 42)
    position = ht._hash_key('fourty-two')
    bt = ht.hashtable[position]
    assert bt.root.data == 42


def test_ht_get_works(ht_nums):
    """ Can we retrieve the data from the hash table?
    """
    assert ht_nums.get('thirtyone') == 31


def test_ht_remove_works(ht_nums):
    """ Can we remove a key-value pair from the hash table?
    """
    assert ht_nums.get('thirtyone') == 31
    assert ht_nums.remove('thirtyone') == 31


def test_ht_remove_returns_false_when_not_present(ht_nums):
    """ We should get a false return if the input key was not present
    """
    assert not ht_nums.remove('fourtytwo')


def test_ht_set_on_collision(collision):
    """ We expect the inputs of collision to have the same hash_key
        But the HashTable should still work.
    """
    assert isinstance(collision, HashTable)


def test_ht_get_on_collision(collision):
    """ We expect the inputs of collision to have the same hash_key
        But the HashTable should still work.
    """
    assert collision.get('sit') is True
    assert collision.get('its') is True


def test_ht_remove_on_collision(collision):
    """ We expect the inputs of collision to have the same hash_key
        But the HashTable should still work.
    """
    assert collision.get('sit') is True
    assert collision.remove('sit') is True
    assert collision.get('sit') is False








