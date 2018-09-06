from .binary_tree import Node, BinaryTree


def find_maximum_value(tree):
    """ Takes binary tree as its only input.
        Return the maximum value stored in the tree.
        We can assume values in Binary Tree are numeric
    """
    # import pdb; pdb.set_trace()
    if not isinstance(tree, BinaryTree):
        raise TypeError('input was not a Binary Tree')

    highest = -float("inf")

    def _walk(node, high):
        """ Helper function to traverse all nodes of the tree
            While traversing, test for max value.
        """
        high = max(node.val, high)
        if node.left:
            print(high)
            high = _walk(node.left, high)
        if node.right:
            print(high)
            high = _walk(node.right, high)
        return high
    if tree.root is None:
        return None
    highest = _walk(tree.root, highest)
    return highest

# if __name__ == '__main__':
