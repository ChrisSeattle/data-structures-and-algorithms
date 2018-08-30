from .stack import Stack, Node
import pytest



def test_alive():
    """ Does the testing file run
    """
    pass


@pytest.fixture
def empty_stack():
    return Stack()

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


def test_stack_str_format_on_empty(empty_stack):
    """ Do we get the expected str return on empty stack
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
    empty_stack.push(42)
    assert len(empty_stack) == expected


def test_stack_push_continues_to_add_multiple_nodes(empty_stack):
    """ Multiple calls to to push method continues to add elements & increment length
    """
    expected = len(empty_stack) + 4
    empty_stack.push(42)
    empty_stack.push(13)
    empty_stack.push(7)
    empty_stack.push(314)
    assert len(empty_stack) == expected
    assert empty_stack.top.val == 314


def test_small_stack_is_valid_stack(small_stack):
    """ We are depending on small_stack, so let's make sure it is a stack data structure
    """
    assert isinstance(small_stack, Stack)


def test_can_instantiate_stack_with_list(small_stack):
    """ Instantiate with a list of four items. Does it report the correct len
        and is the last one added now at the top.
    """
    assert len(small_stack) == 4
    assert small_stack.top.val == 4


def test_declaration_for_each_element_in_iterable_tuple():
    """ If the Stack is instantiated with a tuple, does it
        add a node for each element with last value as top.
    """
    bb = Stack((1, 2, 3))
    assert len(bb) == 3
    assert bb.top.val == 3


def test_stack_str_format_on_not_empty():
    """ Do we get the expected str return when stack has nodes with values
    """
    st = Stack(42)
    expected = 'Top: 42 | Length: 1'
    actual = str(st)
    assert expected == actual


def test_stack_pop_exists():
    """ Is the pop method present in the Stack constructor
    """
    assert Stack.pop


def test_stack_pop_returns_val_of_top(small_stack):
    """ when pop method is called, it shortens the length of the Stack
        and returns the value that was stored at the top position.
    """
    input = 4
    output = small_stack.pop().val
    assert input == output


def test_stack_pop_modifies_length(small_stack):
    """ when pop method is called, it shortens the length of the Stack
        and returns the value that was stored at the top position.
    """
    expected_length = len(small_stack) - 1
    small_stack.pop()
    actual_length = len(small_stack)
    assert expected_length == actual_length


def test_stack_peek_exists():
    """ Is the peek method present in the Stack constructor
    """
    assert Stack.peek


def test_stack_peek_returns_current_top(small_stack):
    """ peek returns the current top without modifying the stack
    """
    val = small_stack.top.val
    assert val == 4
    assert small_stack.peek().val == val


def test_stack_peek_does_not_change_length(small_stack):
    """ peek returns the current top without modifying the stack
    """
    expected_length = len(small_stack)
    small_stack.peek()
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


def test_node_has_expected_next_property_defaults_none():
    """ Does Node have a _next property as expected
    """
    tempNode = Node(42)
    assert tempNode._next is None


def test_node_next_property_can_be_set():
    """ Does Node have a _next property as expected
    """
    tempNode = Node(42)
    newNode = Node(13, tempNode)
    assert newNode._next == tempNode


def test_node_str_return():
    """ Can we create a Node and see that it returns the expected result
        for str
    """
    input_a = 13
    expected_a = str(input_a)
    actual_a = str(Node(input_a))
    assert expected_a == actual_a

