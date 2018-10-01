

def tree_intersection(tree1, tree2):
    """ Find all duplicates in the 2 given BST/BT
        Input is two Binary Trees (or BST)
        Output is a list of duplicates.
    """
    results = dict()
    done = dict()

    def _eval(first, second):
        """ Helper function called recursively
        """
        if first.left is None and first.right is None:
            done[first] = True
        if second.left is None and second.right is None:
            done[second] = True
        if first.val == second.val and first.val not in results:
            results[first.val] = True
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
    return list(results.keys())
