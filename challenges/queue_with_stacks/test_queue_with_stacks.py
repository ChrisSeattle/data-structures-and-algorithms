from .queue_with_stacks import Queue, Stack, Node
import pytest


def test_alive():
    """ Does the testing file run
    """
    pass


@pytest.fixture
def empty_q():
    return Queue()


@pytest.fixture
def small_q2():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    return q


def test_queue_exists():
    """ Do we see Queue
    """
    assert Queue


def test_create_instance_of_queue(empty_q):
    """ can we create a Queue instance with no input values
    """
    assert isinstance(empty_q, Queue)


def test_queue_default_property(empty_q):
    """ Do the default settings work as expected
    """
    assert empty_q.front is None
    assert empty_q.back is None
    assert empty_q._length == 0


def test_queue_enqueue_exists():
    """ Is the enqueue method present in the Queue constructor
    """
    assert Queue.enqueue


def test_queue_add_first_val_successful(empty_q):
    """ Can we insert a single value and see the value in the front position
    """
    empty_q.enqueue(42)
    assert empty_q.front.val == 42
    assert len(empty_q) == 1


def test_queue_add_second_val_successful(empty_q):
    """ Can we insert a single value and see the value in the front position
    """
    empty_q.enqueue(42)
    empty_q.enqueue(13)
    assert empty_q.front.val == 42
    assert empty_q.back.val == 13


def test_queue_add_third_val_successful(empty_q):
    """ Can we insert a single value and see the value in the front position
    """
    empty_q.enqueue(42)
    empty_q.enqueue(13)
    empty_q.enqueue(7)
    assert empty_q.front.val == 42
    assert empty_q.back.val == 7


def test_queue_enque_increases_queue_size(empty_q):
    """ After a value is put into the queue, does length of queue increment
    """
    expected = len(empty_q) + 1
    empty_q.enqueue(42)
    assert len(empty_q) == expected


def test_enqueue_continues_to_add_multiple_nodes(empty_q):
    """ Multiple calls to to enqueue method continues to add elements & increment length
    """
    expected = len(empty_q) + 4
    empty_q.enqueue(42)
    empty_q.enqueue(13)
    empty_q.enqueue(7)
    empty_q.enqueue(314)
    assert len(empty_q) == expected


def test_small_q2_is_valid_queue(small_q2):
    """ We are depending on small_q2, so let's make sure it is a Queue data structure
    """
    assert isinstance(small_q2, Queue)


def test_can_instantiate_queue_with_list(small_q2):
    """ Instantiate with a list of four items. Does it report the correct len
        Is first one at the front and the last one added now at the back.
    """
    assert len(small_q2) == 4
    assert small_q2.front.val == 1
    assert small_q2.back.val == 4


def test_dequeue_exists():
    """ Is the enqueue method present in the enqueue constructor
    """
    assert Queue.dequeue


def test_dequeue_returns_a_node(small_q2):
    """ when dequeue method is called, it shortens the length of the Queue
        and returns the node from the front position
    """
    output = small_q2.dequeue()
    assert isinstance(output, Node)
    # assert output.val == 4


def test_dequeue_modifies_length(small_q2):
    """ when dequeue method is called, it shortens the length of the Queue
        and returns the value that was stored at the front position.
    """
    expected_length = len(small_q2) - 1
    output = small_q2.dequeue()
    actual_length = len(small_q2)
    assert expected_length == actual_length


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

