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

