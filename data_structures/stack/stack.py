from .node import Node
from typing import Any


class Stack(object):
    """ This will create an empty Stack when instantiated, with a
        default None value assigned to 'top'.
        This can also be instantiated with an iterable, creating a Node
        for each value in the iterable.
        The 'len' represents the count of Nodes in the stack at any time.
    """
    def __init__(self, data=None):
        """ Initialize with a None value for top, and _length of 0,
            if no data is passed on instantiating.
            If instantiated with data, create a Node for each iterable value
        """
        self.top: Node = None
        self._length: int = 0
        if data is not None:
            try:
                vals = iter(data)
            except TypeError:
                vals = [data]
            for i in vals:
                current = self.top
                newNode = Node(i, _next=current)
                self.top = newNode
                self._length += 1

    def __len__(self):
        return self._length

    def __str__(self):
        return f'Top: {self.top} | Length: {self._length}'

    def __repr__(self):
        return f'<Top: {self.top} | Length: {self._length}>'

    def push(self, val: Any) -> Any:
        """ Takes val for the value of a Node that is placed as the top
            of the stack with O(1) Time performance.
        """
        newNode = Node(val, _next=self.top)
        self.top = newNode
        self._length += 1
        return f'Added {val} to the top of the stack'

    def pop(self):
        """ Removes and returns the Node currently at the top of the stack
        """
        if self._length == 0:
            return f'The stack has no values'
        temp = self.top
        self.top = temp._next
        temp._next = None
        self._length -= 1
        return temp

    def peek(self):
        """ Reports the top of the stack, but does not change the stack
        """
        return self.top
