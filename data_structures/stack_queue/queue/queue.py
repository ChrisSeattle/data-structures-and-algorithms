from .node import Node
from typing import Any

class Queue(object):
    """
    """
    def __init__(self, data=None):
        """ Initialize Queue with front & back set to None and _length of 0, if no data passed
            If initialized with data, creating add a Node in the Queue for each value in the iterable.
        """
        self.front: Node = None
        self.back: Node = None
        self._length: int = 0
        if data is not None:
            try:
                vals = iter(data)
            except TypeError:
                vals = [data]
            for i in vals:
                newNode = Node(i)
                if self.front is None:  # this is the first node in queue
                    self.front = newNode
                elif self.back is None:  # this is the second node in queue
                    self.front._next, self.back = newNode, newNode
                else:
                    self.back._next, self.back = newNode, newNode
                self._length += 1

    def __len__(self):
        return self._length

    def __str__(self):
        return f'Front: {self.front} | Back: {self.back} | Length: {self._length}'

    def enqueue(self, val):
        """ Adds a node for the passed val and increments _length.
            First in, First out.
        """
        newNode = Node(val)
        if self.front is None:  # this is the first node in queue
            self.front = newNode
        elif self.back is None:  # this is the second node in queue
            self.front._next, self.back = newNode, newNode
        else:
            self.back._next, self.back = newNode, newNode
        self._length += 1

    def dequeue(self):
        """ Returns the node that is in the front of the queue.
            Removes it from the queue and deincrements the _length
        """
        temp = self.front
        self.front = self.front._next
        temp.next = None
        self._length -= 1
        return temp

    def peek(self):
        return self.front



