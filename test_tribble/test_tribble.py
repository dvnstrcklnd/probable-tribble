import pytest

from probable_tribble import rotate_string

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