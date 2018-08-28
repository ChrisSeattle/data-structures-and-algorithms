from .stack import Stack, Node
import pytest


def test_alive():
    """ Does the testing file run
    """
    pass


@pytest.fixture
def empty_stack():
    return Stack([])

@pytest.fixture
def small_stack():
    st = Stack([1, 2, 3, 4])
    return st


def test_stack_exists():
    """ Do we see Stack
    """
    assert Stack


def test_create_instance_of_stack(empty_stack):
    """ can we create a Stack instance with no input values
    """
    assert isinstance(empty_stack, Stack)


def test_default_property_top(empty_stack):
    """ Do the default settings work as expected
    """
    assert empty_stack.top is None
    assert empty_stack._length == 0


def test_stack_str_format(empty_stack):
    """ Do we get the expected str return
    """
    expected = 'Top: None | Length: 0'
    actual = str(empty_stack)
    assert expected == actual


def test_stack_push_exists():
    """ Is the push method present in the Stack constructor
    """
    assert Stack.push


def test_stack_push_on_val_successful(empty_stack):
    """ Can we insert a single value and see the value in the top position
    """
    empty_stack.push(42)
    assert empty_stack.top.val == 42


def test_stack_push_increases_stack_size(empty_stack):
    """ After a value is pushed to the stack, does length of stack increment
    """
    expected = len(empty_stack) + 1
    empty_stack(42)
    assert len(empty_stack) == expected


def test_can_instantiate_stack_with_list(small_stack):
    """ Instantiate with a list of four items. Does it report the correct len
        and is the last one added now at the top.
    """
    assert len(small_stack) == 4
    assert small_stack.top.val == 4


def test_insertion_for_each_element_in_iterable_tuple():
    """ If the Stack is instantiated with a tuple, does it
        add a node for each element?
    """
    bb = Stack((1, 2, 3))
    assert len(bb) == 3
    assert bb.top.val == 3


def test_stack_pop_exists():
    """ Is the pop method present in the Stack constructor
    """
    assert Stack.pop


def test_stack_pop_returns_val_of_top_and_modifies_length(small_stack):
    """ when pop method is called, it shortens the length of the Stack
        and returns the value that was stored at the top position.
    """
    expected_length = len(small_stack) - 1
    assert small_stack.pop == 4
    assert expected_length == len(small_stack)


def test_node_exists():
    """ Can we see Node
    """
    assert Node


def test_node_holds_expected_values():
    """ Can we create a Node and see that it the value we passed to it
        is returned as expected by the Node
    """
    input_b = 42
    expected_b = str(input_b)
    actual_b = str(Node(input_b))
    assert expected_b == actual_b


def test_node_str_return():
    """ Can we create a Node and see that it returns the expected result
        for str
    """
    input_a = 13
    expected_a = str(input_a)
    actual_a = str(Node(input_a))
    assert expected_a == actual_a
