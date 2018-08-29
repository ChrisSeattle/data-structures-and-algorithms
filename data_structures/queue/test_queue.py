from .queue import Queue, Node
import pytest


def test_alive():
    """ Does the testing file run
    """
    pass


@pytest.fixture
def empty_q():
    return Queue()

@pytest.fixture
def small_q():
    q = Queue([1, 2, 3, 4])
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


def test_queue_str_format_on_empty(empty_q):
    """ Do we get the expected str return on empty queue
    """
    expected = 'Front: None | Back: None | Length: 0'
    actual = str(empty_q)
    assert expected == actual


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


def test_small_q_is_valid_queue(small_q):
    """ We are depending on small_q, so let's make sure it is a Queue data structure
    """
    assert isinstance(small_q, Queue)


def test_can_instantiate_queue_with_list(small_q):
    """ Instantiate with a list of four items. Does it report the correct len
        Is first one at the front and the last one added now at the back.
    """
    assert len(small_q) == 4
    assert small_q.front.val == 1
    assert small_q.back.val == 4


def test_declaration_for_each_element_in_iterable_tuple():
    """ If the queue is instantiated with a tuple, does it
        add a node for each element with last value as top.
    """
    bb = Queue((1, 2, 3))
    assert len(bb) == 3
    assert bb.back.val == 3
    assert bb.front.val == 1


def test_queue_str_format_on_one_element(empty_q):
    """ Do we get the expected str return when queue has 1 Node with a value
    """
    q = Queue(42)
    expected = 'Front: 42 | Back: None | Length: 1'
    actual = str(q)
    assert expected == actual
    qq = empty_q
    qq.enqueue(42)
    actual = str(qq)
    assert expected == actual


def test_queue_str_format_on_two_element(empty_q):
    """ Do we get the expected str return when Queue has 2 Nodes with a value
    """
    q = Queue((42, 13))
    expected = 'Front: 42 | Back: 13 | Length: 2'
    actual = str(q)
    assert expected == actual
    qq = empty_q
    qq.enqueue(42)
    qq.enqueue(13)
    actual = str(qq)
    assert expected == actual


def test_queue_str_format_on_three_element(empty_q):
    """ Do we get the expected str return when Queue has 3 Nodes with a value
    """
    q = Queue([42, 13, 7])
    expected = 'Front: 42 | Back: 7 | Length: 3'
    actual = str(q)
    assert expected == actual
    empty_q.enqueue(42)
    empty_q.enqueue(13)
    empty_q.enqueue(7)
    actual = str(empty_q)
    assert expected == actual


def test_dequeue_exists():
    """ Is the enqueue method present in the enqueue constructor
    """
    assert Queue.dequeue


def test_dequeue_returns_a_node(small_q):
    """ when dequeue method is called, it shortens the length of the Queue
        and returns the node from the front position
    """
    output = small_q.dequeue()
    assert isinstance(output, Node)
    # assert output.val == 4


def test_dequeue_modifies_length(small_q):
    """ when dequeue method is called, it shortens the length of the Queue
        and returns the value that was stored at the front position.
    """
    expected_length = len(small_q) - 1
    output = small_q.dequeue()
    actual_length = len(small_q)
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

