from .array_shift import insert_shift_array


def test_insert_shift_array_exists():
   """ Docstring needed for tests?
   From class examples, it seems they are not needed.
   """
   assert insert_shift_array


def test_value_inserted_into_even_list():
    expected = [1, 2, 5, 3, 4]
    actual = insert_shift_array([1, 2, 3, 4], 5)
    assert actual == expected


def test_value_inserted_into_odd_list():
    expected = [1, 2, 3, 7, 4, 5, 6]
    actual = insert_shift_array([1, 2, 3, 4, 5, 6], 7)
    assert actual == expected

