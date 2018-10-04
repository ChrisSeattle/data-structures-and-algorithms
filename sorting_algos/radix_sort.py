
def radix_sort(arr):
    """ implement a radix sort
    """
    base = 10
    i = 0
    work = arr[:]

    while True:
        buckets = [[] for _ in range(base)]
        i += 1
        for val in work:
            idx = val % (base**i)
            idx = idx // (base**(i-1))
            buckets[idx].append(val)
        if len(buckets[0]) < len(work):
            work = [elem for bucket in buckets for elem in bucket]
        else:
            return buckets[0]


# if __name__ == '__main__':
#     do stuff
