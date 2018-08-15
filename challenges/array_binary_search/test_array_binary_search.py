from .array_binary_search import binary_search


def test_binary_search_exists():
    assert binary_search


def test_binary_search_when_val_not_present_but_inside_max_and_min_array_value():
    expected = -1
    test_arr = [2, 4, 6, 8, 10]
    test_val = 9
    assert expected == binary_search(test_arr, test_val)


def test_binary_search_when_val_less_than_lowest_element_value():
    expected = -1
    test_arr = [2, 4, 6, 8, 10, 15, 16, 32, 10001]
    test_val = 1
    assert expected == binary_search(test_arr, test_val)


def test_binary_search_when_val_greater_than_highest_element_value():
    expected = -1
    test_arr = [2, 4, 6, 8, 10, 11, 12, 13, 72, 100, 500]
    test_val = 1100
    assert expected == binary_search(test_arr, test_val)


def test_binary_search_when_val_exists_in_second_quartile():
    expected = 5
    test_arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]
    test_val = 11
    assert expected == binary_search(test_arr, test_val)


def test_binary_search_when_val_exists_in_third_quartile():
    expected = 5
    test_arr = [1,2,3,4,5,6,7,8]
    test_val = 6
    assert expected == binary_search(test_arr, test_val)

