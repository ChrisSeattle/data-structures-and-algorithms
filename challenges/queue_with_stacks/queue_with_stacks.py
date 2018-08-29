from .stack.stack import Stack, Node
# It would be nicer to import from data_structures


class Queue(object):
    """ Implement a Queue using two Stacks.
    """
    def __init__(self):
        """
        """
        self.back = None
        self.front = None
        self._length = 0
        self.input = Stack()
        self.flipped = Stack()

    def __len__(self):
            return self._length

    def enqueue(self, value):
        """ First in, first out is our goal. However we are using stacks
            which are last in, first out. For our initital storage, this
            doesn't matter very much.
        """
        if self._length == 0:
            self.front = self.input.push(value)
        else:
            self.back = self.input.push(value)
        self._length += 1
        return self


    def dequeue(self):
        """ First in, first out is our goal. Since data is stored in a Stack
            we are going to move all of the nodes to a new stack such that
            it is in reverse of the original. By using Stack.pop from this
            flipped (reversed) stack we will capture the previously first
            node. We account for the shorter Queue and flip it back so we
            are ready for any new enqueued data.
        """
        # while self.input._length > 0:
        for i in range(self._length):
            self.flipped.push(self.input.pop())
        # This means flipped Stack is a reverse of input Stack
        output = self.flipped.pop()
        # thanks to Stack.pop, output is a Node w/ ._next set to None.
        self._length -= 1
        # Our Queue is now 1 shorter, but we need to flip it back
        for i in range(self._length):
            if i == 0:
                self.front = self.input.push(self.flipped.pop())
            else:
                self.back = self.input.push(self.flipped.pop())
        return output

