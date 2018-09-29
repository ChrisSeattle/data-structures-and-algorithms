# from textwrap import dedent
import sys


def selection_sort(arr):
    """ Sorts an array by repeatedly finding the minimum element (considering
        ascending order) from unsorted part and putting it at the beginning.
        This implementation is an in-place sort.
    """
    for j in range(0, len(arr)-1):
        min_idx = j
        # import pdb; pdb.set_trace()
        for i in range(j+1, len(arr)):
            if arr[min_idx] > arr[i]:
                min_idx = i
        arr[j], arr[min_idx] = arr[min_idx], arr[j]
    return arr


# if __name__ == '__main__':
#     do stuff
