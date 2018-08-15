
def binary_search(arr, val):
    """With the given array, return the index position of the given value,
    if it exists in the array. If it is not in the array, return -1.
    """
    max = len(arr)
    min = 0
    while True:
        mid = (max - min) // 2 + min
        if val == arr[mid]:
            return mid
        if val < arr[mid]:
            if max == mid: return -1
            max = mid
        if val > arr[mid]:
            if min == mid: return -1
            min = mid



def run():
    """This is the main function, which calls the other functions to do the main work
    """
    arr = [int(i) for i in input().split()]
    val = int(input())
    print(binary_search(arr, val))


if __name__ == '__main__':
    run()


