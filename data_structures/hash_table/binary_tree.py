

class Node(object):
    """ Node used in Binary tree. Is aware of a left and a right
        for following Nodes, holds a value and data.
        If no data is given, data will be set to the given val
    """
    def __init__(self, val, data=None, left=None, right=None):
        self.val = val
        if data is None:
            data = val
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
            if isinstance(iterable, dict):
                [self.insert(val, data) for val, data in iterable.items()]
            else:
                try:
                    iterable = iter(iterable)
                except TypeError:
                    iterable = [iterable]
                for i in iterable:
                    # if isinstance(i, dict):
                    #     vals, data = i.items()
                    #     for j in range(len(i)):
                    #         self.insert(vals[j], data[j])
                    # else:
                    self.insert(i)

    def __str__(self):
        return f'BinaryTree | Root: {self.root}'

    def __repr__(self):
        return f'<BinaryTree | Root: {self.root}>'

    def insert(self, val, data=None):
        """ Insert new value at appropriate tree location (but not self-correcting)
            Val is the location key, data is stored info (if none given, use val)
            Insert with O(log n)
        """
        if data is None:
            data = val

        def _walk(curr, val, data):
            """ This recursive helper function will drill down to an insertion point
                Returns True if we were able to insert, False if we have a duplicate val
            """
            if val < curr.val:
                if curr.left is None:
                    curr.left = Node(val, data)
                    return True
                return _walk(curr.left, val, data)
            if val > curr.val:
                if curr.right is None:
                    curr.right = Node(val, data)
                    return True
                return _walk(curr.right, val, data)
            else:
                raise ValueError(f'Neither < or > for {val}, {curr.val}')
                # return False

        if self.root is None:
            self.root = Node(val, data)
            return True
        _walk(self.root, val, data)
    # end of insert

    def insert_node(self, n):
        """ Insert an already made node that has a n.val and a n.data at appropriate tree location
            Val is the location key, data is stored info (if none given, use val)
            Insert with O(log n)
        """
        if not isinstance(n, Node):
            raise TypeError(f'Not a valid Node type')

        if n.data is None:
            n.data = n.val

        def _walk(curr, n):
            """ This recursive helper function will drill down to an insertion point
                Returns True if we were able to insert, False if we have a duplicate val
            """
            if n.val < curr.val:
                if curr.left is None:
                    curr.left = n
                    return True
                return _walk(curr.left, n)
            if n.val > curr.val:
                if curr.right is None:
                    curr.right = n
                    return True
                return _walk(curr.right, n)
            else:
                raise ValueError(f'Neither < or > for {n.val}, {curr.val}')
                # return False

        if self.root is None:
            self.root = n
            return True
        return _walk(self.root, n)
    # end of insert_node

    def get(self, val):
        """ Searches for the val, returns the data
        """
        if self.root is None:
            return False

        def _walk(curr, val):
            """ This recursive helper function will drill down to find a node location
                Returns the data value if found, returns False if it is not present
            """
            if val == curr.val:
                return curr.data
            if val < curr.val:
                if curr.left is None:
                    return False
                return _walk(curr.left, val)
            if val > curr.val:
                if curr.right is None:
                    return False
                return _walk(curr.right, val)
            else:
                raise ValueError(f'Neither < or > for {val}, {curr.val}')
                # return False

        return _walk(self.root, val)

    def delete(self, val):
        """ Find a node by the val, and remove it from the tree
        """

        def _walk(curr, val, prev=None):
            """ This recursive helper function will drill down to find a node location
                Returns the data value if found, returns False if it is not present
            """
            if val == curr.val:
                if prev is not None and prev.left == curr:
                    prev.left = None
                if prev is not None and prev.right == curr:
                    prev.right = None
                if curr.left is not None:
                    self.insert_node(curr.left)
                if curr.right is not None:
                    self.insert_node(curr.right)
                return curr.data
            if val < curr.val:
                if curr.left is None:
                    return False
                return _walk(curr.left, val, curr)
            if val > curr.val:
                if curr.right is None:
                    return False
                return _walk(curr.right, val, curr)
            else:
                raise ValueError(f'Neither < or > or == for {val}, {curr.val}')
                # return False

        return _walk(self.root, val)


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
