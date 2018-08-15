def insert_shift_array(arr, val):
    ind = len(arr) // 2 + len(arr) % 2
    return arr[:ind] + [val] + arr[ind:]


def run():
    arr = input().split()
    val = str(input())
    print(insert_shift_array(arr, val))


if __name__ == '__main__':
    run()
