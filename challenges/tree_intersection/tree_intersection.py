# from textwrap import dedent
# import sys


# from .queue.queue import Queue, Node


class Node(object):
    """ Node used in Binary tree. Is aware of a left and a right
        for following Nodes, holds a value and data.
    """
    def __init__(self, val, data=None, left=None, right=None):
        self.val = val
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return f'{self.val}'

    def __repr__(self):
        return f'<Node | Val: {self.val} | Data: {self.data} | Left: {self.left} | Right: {self.right}>'


class Queue(object):
    """ This Queue works with Nodes as both inputs and outputs.
    """
    def __init__(self):
        """ Initialize Queue with front & back set to None and _length of 0.
            This version of Queue will not take in any initital values or Nodes.
        """
        self.front = None
        self.back = None
        self._length = 0


    def __len__(self):
        return self._length

    def __str__(self):
        return f'Front: {self.front} | Back: {self.back} | Length: {self._length}'

    def __repr__(self):
        return f'<Front: {self.front} | Back: {self.back} | Length: {self._length}>'

    def enqueue(self, newNode):
        """ Adds a node for the passed val and increments _length.
            First in, First out.
        """
        if self.front is None:  # this is the first node in queue
            self.front, self.back = newNode, newNode
        elif self.back is self.front:  # this is the second node
            self.front._next, self.back = newNode, newNode
        else:
            self.back._next, self.back = newNode, newNode
            newNode._next = None
        self._length += 1

    def dequeue(self):
        """ Returns the node that is in the front of the queue.
            Removes it from the queue and deincrements the _length
        """
        temp = self.front
        self.front = self.front._next
        temp._next = None
        self._length -= 1
        return temp

    def peek(self):
        return self.front


class BinaryTree(object):
    """ Accepts an iterable object and makes a node for each value
        From this data it creates a tree.
    """
    def __init__(self, iterable=None):
        self.root = None
        if iterable is not None:
            try:
                iterable = iter(iterable)
            except TypeError:
                iterable = [iterable]
            for i in iterable:
                self.insert(i)

    def __str__(self):
        return f'BinaryTree | Root: {self.root}'

    def __repr__(self):
        return f'<BinaryTree | Root: {self.root}>'

    def insert(self, val):
        """ Insert new value at appropriate tree location (but not self-correcting)
            Insert with O(log n)
        """
        def _walk(curr, val):
            """ This recursive helper function will drill down to an insertion point
                Returns True if we were able to insert, False if we have a duplicate val
            """
            if val < curr.val:
                if curr.left is None:
                    curr.left = Node(val)
                    return True
                return _walk(curr.left, val)
            if val > curr.val:
                if curr.right is None:
                    curr.right = Node(val)
                    return True
                return _walk(curr.right, val)
            else:
                raise ValueError(f'Neither < or > for {val}, {curr.val}')
                # return False

        if self.root is None:
            self.root = Node(val)
            return True
        _walk(self.root, val)
    # end of insert method

    def in_order(self, callable=lambda node: print(node)):
        """ Go left, visit, then go right
        """
        def _walk(node=None):
            if node is None:
                return
            # Go Left
            if node.left is not None:
                _walk(node.left)
            # Visit
            callable(node)
            # Go Right
            if node.right is not None:
                _walk(node.right)
        _walk(self.root)

    def pre_order(self, callable=lambda node: print(node)):
        """ Vist, Go left, then go right
        """
        def _walk(node=None):
            if node is None:
                return
            # Visit
            callable(node)
            # Go Left
            if node.left is not None:
                _walk(node.left)
            # Go Right
            if node.right is not None:
                _walk(node.right)
        _walk(self.root)

    def post_order(self, callable=lambda node: print(node)):
        """ Go left, then go right, visit
        """
        def _walk(node=None):
            if node is None:
                return
            # Go Left
            if node.left is not None:
                _walk(node.left)
            # Go Right
            if node.right is not None:
                _walk(node.right)
            # Visit
            callable(node)
        _walk(self.root)

    def breadth_first(self):
        """ breadth first traversal. Uses a helper function
            called _walk and a Queue to help us view and track all
            nodes in our binary tree. This Queue is designed to
            accept Nodes as inputs & outputs to enqueue & dequeue
        """
        q = Queue()
        def _walk(q):
            if q.front.left:
                q.enqueue(q.front.left)
            if q.front.right:
                q.enqueue(q.front.right)
            print(q.dequeue().val)
            if q.front is None:
                return
            _walk(q)

        q.enqueue(self.root)
        _walk(q)


def tree_intersection(tree1, tree2):
    """ Find all duplicates in the 2 given BST/BT
        Input is two Binary Trees (or BST)
        Output is a list of duplicates.
    """
    results = []
    done = dict()

    def _eval(first, second):
        """ Helper function called recursively
        """
        if first.left is None and first.right is None:
            done[first] = True
        if second.left is None and second.right is None:
            done[second] = True
        if first.val == second.val:
            results.append(first.val)
            return
        if first.val > second.val:
            if second.right is not None and second.right not in done:
                _eval(first, second.right)
            if first.left is not None and first.left not in done:
                _eval(first.left, second)
            return
        if first.val < second.val:
            if first.right is not None and first.right not in done:
                _eval(first.right, second)
            if second.left is not None and second.left not in done:
                _eval(first, second.left)
            return

    _eval(tree1.root, tree2.root)
    return results


# if __name__ == '__main__':
#     do stuff
