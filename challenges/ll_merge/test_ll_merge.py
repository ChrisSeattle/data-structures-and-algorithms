from .ll_merge import merge_lists, LinkedList, Node
import pytest


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
    # values in Node order: 4 3 2 1 (null)
    return ll

@pytest.fixture
def med_list():
    ll = LinkedList([])
    ll.insert('a')
    ll.insert('b')
    ll.insert('c')
    ll.insert('d')
    ll.insert('e')
    ll.insert('f')
    # values in Node order: f, e, d, c, b, a
    return ll


def test_alive():
    """ Does the testing file run
    """
    pass


# New tests

def test_linked_list_ll_merge_exists():
    """ Test ll_merge exists
    """
    assert merge_lists


def test_merge_lists_basic_works():
    a = LinkedList(1)
    b = LinkedList(2)
    expected = LinkedList([2, 1])
    actual = merge_lists(a, b)
    print(expected)
    print(actual)
    assert expected == actual

def test_linked_list_merge_returns_not_valid_list(empty_list):
    """ assert empty lists give back None
    """
    expected = None
    actual = merge_lists(empty_list, empty_list)
    assert expected == actual


def test_linked_list_merge_merges_lists_equal_lengths(small_list, empty_list):
    """ Test empty list and list input gives back list
    """
    expected = small_list
    actual = merge_lists(small_list, empty_list)
    assert expected == actual


def test_linked_list_merge_merges_lists_equal_lengths_other(small_list):
    """ Test empty list and list input gives back list
    """
    r = LinkedList([])
    a = LinkedList([])
    b = LinkedList([])
    a.insert(1)
    r.insert(1)
    b.insert(2)
    r.insert(2)
    a.insert(3)
    r.insert(3)
    b.insert(4)
    r.insert(4)
    actual = merge_lists(a, b)
    assert r == actual


# End new tests

# Old tests

def test_kth_from_end_exists():
    """ is the method kth_from_end present and can we see it
    """
    assert LinkedList.kth_from_end


def test_kth_from_end_exception_on_list_too_short(small_list):
    """ Do we get an exemption if our linked list is not big enough to
        look k positions back?
    """
    expected = 'exception'
    actual = small_list.kth_from_end(101)
    assert expected == actual


def test_kth_from_end_when_target_last_node(small_list):
    """ If k is 0, then do we get the last node as expected
    """
    expected = 1
    actual = small_list.kth_from_end(0)
    assert expected == actual


def test_kth_from_end_item_when_target_is_head(small_list):
    """ If our target is the Head of the LinkedList, do we get expected result
    """
    expected = 4
    actual = small_list.kth_from_end(3)
    assert expected == actual


def test_kth_from_end_item_middle_num(small_list):
    """ If our target is in a position in the middle, doe we get expected result
    """
    expected = 2
    actual = small_list.kth_from_end(1)
    assert expected == actual


def test_kth_from_end_empty_list(empty_list):
    """ If the LinkedList has no nodes, we should get an
        exception response
    """
    expected = 'exception'
    actual = empty_list.kth_from_end(45)
    assert expected == actual


# -- Tests from Previous Work --

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


def test_linked_list_includes_all_input_elements():
    """ Is the includes method able to identify if a the value is in the LinkedList
        for all values that we had put in the list (only a a size of a few elements tested)
    """
    a = [5,6,7,8]
    aa = LinkedList([])
    aa.insert(a)
    for i in a:
        assert aa.includes(i) is True
    assert len(aa) == len(a)


def test_node_exists():
    """ Can we see Node
    """
    assert Node


def test_node_str_return():
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


def test_linked_list_instantiates_with_list_input():
    """ Can we instantiate a LinkedList and pass it an iterable input such that
        for each element a node is created to store that value
    """
    a = [5,6,7,8]
    aa = LinkedList(a)
    # for i in a:
    #     assert aa.includes(i) is False
    assert len(aa) == len(a)
    assert aa.includes(5)
    assert aa.includes(6)
    assert aa.includes(7)
    assert aa.includes(8)

