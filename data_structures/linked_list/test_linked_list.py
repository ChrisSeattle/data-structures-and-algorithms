from .linked_list import LinkedList, Node
import pytest


def test_alive():
    """ Does the testing file run
    """
    pass


@pytest.fixture
def empty_list():
    return LinkedList([])


@pytest.fixture
def small_list():
    ll = LinkedList([])
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    return ll


def test_linked_list_exists():
    """ Do we see LinkedList
    """
    assert LinkedList


def test_create_instance_of_list(empty_list):
    """ can we create a LinkedList instance
    """
    assert isinstance(empty_list, LinkedList)


def test_default_property_head(empty_list):
    """ Do the default settings work as expected
    """
    assert empty_list.head == None
    assert empty_list._length == 0


def test_linked_list_str_format(empty_list):
    """ Do we get the expected str return
    """
    expected = 'Head: None | Length: 0'
    actual = str(empty_list)
    assert expected == actual


def test_linked_list_repr_format(empty_list):
    """ Does the repr get the exprected result
    """
    expected = '<Linked List | Head: None | Length: 0>'
    actual = repr(empty_list)
    assert expected == actual


def test_linked_list_insert_exists():
    """ Is the insert method present in the LinkedList constructor
    """
    assert LinkedList.insert


def test_linked_list_insertion_on_single_val_successful(empty_list):
    """ Can we insert a single value and see the value in the head position
        and see the length of LinkedList increase
    """
    empty_list.insert(42)
    assert empty_list.head.val == 42
    assert len(empty_list) == 1


def test_length_of_list_increases_after_few_single_val_insertion(small_list):
    """ After a few single value insertions, is the most recent value stored in
        the head node and does the length of the list increase accordingly
    """
    assert len(small_list) == 4
    assert small_list.head.val == 4


def test_insertion_for_each_element_input_list(empty_list):
    """ If the insert function recieves an iterable list, does the LinkedList add
        a node for each element in that list
    """
    a = [5,6,7,8]
    empty_list.insert(a)
    assert len(empty_list) == len(a)


def test_insertion_for_each_element_in_iterable_tuple(empty_list):
    """ If the insert function recieves a tuple as iterable, does the LinkedList
        add a node for each element?
    """
    b = (1, 2, 3)
    bb = LinkedList([])
    bb.insert(b)
    assert len(bb) == 3


def test_linked_list_includes_exists():
    """ Does the includes method exist in LinkedList
    """
    assert LinkedList.includes


def test_linked_list_includes_works_last_node(small_list):
    """ After inserting a few nodes with given values, are we able to identify if
        the value we know in the last node is included in the list
    """
    assert small_list.includes(1) is True


def test_linked_list_includes_all_insert_elements():
    """ Is the includes method able to identify if a the value is in the LinkedList
        for all values that we had put in the list (only a lift of a few elements tested)
    """
    a = [5,6,7,8]
    aa = LinkedList([])
    aa.insert(a)
    for i in a:
        assert aa.includes(i) is True
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 4200f89307865023004a4dc117de662123105636
    assert len(aa) == len(a)


def test_linked_list_returns_false_for_includes_val_not_in_list(small_list):
    assert small_list.includes(42) is False
    assert small_list.includes(0) is False


def test_linked_list_instantiates_with_list_input():
    """ Can we instantiate a LinkedList and pass it an iterable input such that
        for each element a node is created to store that value
    """
    a = [5,6,7,8]
    aa = LinkedList(a)
    for i in a:
        assert aa.includes(i) is True
<<<<<<< HEAD
>>>>>>> ee6330cff13d5e1b1b51d69e4dc660e9fa7896f9
=======
>>>>>>> 4200f89307865023004a4dc117de662123105636
    assert len(aa) == len(a)


def test_linked_list_instantiates_with_tuple_input():
    """ If the LinkedList is instantiated with a a tuple as iterable, does the
        LinkedList add a node for each element?
    """
    b = (1, 2, 3)
    bb = LinkedList(b)
    assert len(bb) == 3


def test_linked_list_instantiated_with_values_returns_includes_false_for_val_not_in_list():
    """ After instantiating the LinkedList with a list input (to create a Node for each element),
        we should get a false for testing if the LinkedList includes values not in that list
    """
    b = [9, 10, 11, 12]
    bb = LinkedList(b)
    assert bb.includes(42) is False


def test_node_exists():
    """ Can we see Node
    """
    assert Node


def test_node_str_return_and_node_holds_expected_values():
    """ Can we create a Node and see that it the value we passed to it
        is returned as expected by the Node
    """
    input_a = [7, 13, 42]
    input_b = 42
    expected_a = str(input_a)
    expected_b = str(input_b)
    actual_a = str(Node(input_a))
    actual_b = str(Node(input_b))
    assert expected_a == actual_a
    assert expected_b == actual_b


def test_node_repr_return():
    """ If we create a Node do we see the repr output that we expect
    """
    input = 42
    expected = f'<Node | Val: {input} | Next: None>'
    actual = repr(Node(input))
    assert expected == actual


