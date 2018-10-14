
def merge_sort(arr):
    """ Implementation of a merge_sort algorithm using recursion.
    """

    def _merge(a, b):
        """ This will be recalled recursevly.
            Takes in two pre-sorted arrays and returns a single sorted array.
        """
        i = 0
        j = 0
        k = 0
        r = [[] for _ in range(len(a)+len(b))]

        while i < len(a) and j < len(b):
            # import pdb; pdb.set_trace()
            if b[j] < a[i]:
                r[k] = b[j]
                j += 1
            else:
                r[k] = a[i]
                i += 1
            k += 1

        while i < len(a):
            r[k] = a[i]
            k += 1
            i += 1
        while j < len(b):
            r[k] = b[j]
            k += 1
            j += 1

        return r
        # end _merge helper function

    if len(arr) > 1:
        mid = len(arr) // 2
        a = merge_sort(arr[:mid])
        b = merge_sort(arr[mid:])
        return _merge(a, b)
    return arr
