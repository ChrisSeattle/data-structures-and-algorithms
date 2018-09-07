from .this_directory import function_name, other_function
from ... top.middle.lower.filename import Class1, Class2
import pytest


def test_alive():
    """ Does our test file even run
    """
    pass


def test_function_name_exists():
    """ can we see the basic function
    """
    assert function_name



@pytest.fixture
def empty_list():
    return Class1()


@pytest.fixture
def small_list():
    sl = Class2()
    sl.insert(1)
    sl.insert(2)
    sl.insert(3)
    sl.insert(4)
    return sl


def test_function_name_results_are_a_certain_way(empty_list):
    """ docstring on what we are checking
    """
    expected = 44
    actual = empty_list.method(44)
    assert expected == actual

