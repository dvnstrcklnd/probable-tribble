import pytest

from probable_tribble import (rotate_string,
                              count_above_below)

@pytest.mark.parametrize("string, number, expect", [
    ("MyString", 2, "ngMyStri"),
    ("MyString", -2, "StringMy"),
    ("Hello World", 0, "Hello World"),
    ("Foo", 3, "Foo")
])
def test_rotate_string(string, number, expect):
    output = rotate_string(string, number)
    assert output == expect

@pytest.mark.parametrize("string, number", [
    ("Foo", 4)
])
def test_rotate_string_error(string, number):
    with pytest.raises(IndexError):
        rotate_string(string, number)

@pytest.mark.parametrize("lst, val, expect_below, expect_above", [
    ([1,2,3,4,5], 2, 1, 3),
    ([1,2,3,4,5], 3, 2, 2),
    ([1,2,3,4,5], 4, 3, 1),
    ([1,2,3,4,5], 6, 5, 0),
    ([1,2,3,4,5], 0, 0, 5)
])
def test_count_above_below(lst, val, expect_below, expect_above):
    below, above = count_above_below(lst, val)
    assert below == expect_below
    assert above == expect_above
