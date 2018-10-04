

def quick_sort(arr):
    """ Sorts an array by choosing a pivot point, then placing all values
        less than the pivot point value before the pivot point, and all
        values greater than the pivot point value after the pivot point.
        Returns a list in acescending order.
    """

    if len(arr) < 2:
        return arr
    p = len(arr) // 2
    lo = []
    hi = []
    i = -1
    while i < len(arr) - 1:
        # import pdb; pdb.set_trace()
        i += 1
        if i == p:
            continue
        if arr[i] > arr[p]:
            hi.append(arr[i])
        else:  # Note: equal values go into lo
            lo.append(arr[i])
    hi = quick_sort(hi)
    lo = quick_sort(lo)
    lo.append(arr[p])
    if len(hi) > 0:
        lo = lo + hi
    return lo
