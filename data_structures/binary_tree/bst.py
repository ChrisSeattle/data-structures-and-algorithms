
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
