def insert_shift_array(arr, val):
    """Takes in an list, and a value.
    Returns a new array that is much like the original array but
    now the given value is in the middle of our retruned array.
    """
    ind = len(arr) // 2 + len(arr) % 2
    return arr[:ind] + [val] + arr[ind:]


def run():
    """ If this file was called directly, ask for a list, then
    ask for a value we want inserted in the middle of that list.
    Then call the insert_shift_array function with those values
    """
    arr = input().split()
    val = str(input())
    print(insert_shift_array(arr, val))


if __name__ == '__main__':
    """ Check if called, then execute the main run function
    """
    run()
