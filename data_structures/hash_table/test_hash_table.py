from .hash_table import HashTable
import pytest


def test_alive():
    """ Does our test file even run
    """
    pass


def test_class_name_exists():
    """ can we see the class
    """
    assert HashTable


@pytest.fixture
def empty():
    return HashTable()


@pytest.fixture
def collision():
    value = 'tis sit its sit'
    h = HashTable()
    h.set(value)
    return h



