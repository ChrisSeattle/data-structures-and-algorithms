from .node import Node
from typing import Any


class LinkedList(object):
    # """ Will take in a list of values.
    #     This will create a Node for each element in that list.
    #     The value stored in each Node will be the value of the element for which it was created.
    # """

    def __init__(self):
        self.head: Node = None # the ': Node' sets the datatype, it is optional.
        self._length: int = 0


    def __str__(self):
        return f'Head: {self.head} | Length: {self._length}'

    def __repr__(self):
        return f'<Linked List | Head: {self.head} | Length: {self._length}>'

    def __len__(self):
        return self._length

    def __iter__(self):
        pass

    def __next__(self):
        # self._next
        pass


    def insert(self, val: Any) -> Any:
        current = self.head
        newNode = Node(val, _next=current)
        self.head = newNode
        self._length += 1


    def includes(self, val: Any) -> bool: #the arrow datatype says it returns that datatype
        # search through each node to see if that nodes value is equal to val
        # if one is found, return a bool True
        # if the val is not in the val for any Node, return a bool False
        current = self.head
        while current.next is not None:
            if current.val == val:
                return True
            current = current.next
        return False

