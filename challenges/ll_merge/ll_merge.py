from .node import Node
from typing import Any


class LinkedList(object):
    """ Will take in a list of values.
        This will create a Node for each element in that list.
        The value stored in each Node will be the value of the element for which it was created.
    """

    def __init__(self, data):
        self.head: Node = None # the ': Node' sets the datatype, it is optional.
        self._length: int = 0
        try:
            vals = iter(data)
        except TypeError:
            vals = [data]
        for i in vals:
            current = self.head
            newNode = Node(i, _next=current)
            self.head = newNode
            self._length += 1

        # try:
        #     self.insert(val_list)
        # except TypeError:
        #     return 'Sorry, input values are not valid'

    def __str__(self):
        return f'Head: {self.head} | Length: {self._length}'

    def __repr__(self):
        return f'<Linked List | Head: {self.head} | Length: {self._length}>'

    def __len__(self):
        return self._length

    def __iter__(self):
        return self

    def __next__(self):
        return self._next

    def insert(self, val: Any) -> Any:
        """ If input is a iterable, for each element create a node with that value
            If input is a single value, create a node with that value
            In their original order, each new node is inserted at the Head of the LinkedList
            Meaning the last value of a iterable (like a list) will be the value at Head
        """
        try:
            vals = iter(val)
        except TypeError:
            vals = [val]
        for i in vals:
            current = self.head
            newNode = Node(i, _next=current)
            self.head = newNode
            self._length += 1

    def includes(self, val: Any) -> bool: #the arrow datatype says it returns that datatype
        """ Search through each node to see if that nodes value is equal to val
            If one is found, return a bool True. If the val is not in the val for any Node, return a bool False
        """
        current = self.head
        while True:
            if current.val == val:
                return True
            if current._next is None:
                break
            current = current._next
        return False

    def kth_from_end(self, k):
        """ For a given k, find the node that is k from the end of the
            linked list (count starting with 0)
        """
        if self.head is None:
            return 'exception'
        current = self.head
        counter = 0
        while current._next is not None:
            current = current._next
            counter += 1
        if k > counter:
            return 'exception'
        r, counter = counter - k, 0
        current = self.head
        print(counter, ": ", current.val)
        while counter < r:
            current = current._next
            counter += 1
            print(counter, ": ", current.val)
        return current.val

    def merge_lists(self, inp2):
        """ Takes in two LinkedLists and returns one LinkedList that is the nodes
            of the inputs placed in alternating order (starting with the beginning
            of inp1). This should work as long as both inputs are non-circular
            LinkedLists of any length.
        """
        if self.head is None:
            if inp2.head is None:
                return None
            return inp2
        if inp2.head is None:
            return self
        curr, curr2 = self.head, inp2.head

        while True:
            if curr._next is None:
                curr._next = curr2
                break
            temp, curr._next = curr._next, curr2
            if curr2._next is None:
                curr2._next = temp
                break
            temp2, curr2._next = curr2._next, temp
            curr, curr2 = temp, temp2
            print(curr)
            print(curr2)
        return self
