import pytest

from probable_tribble import main

@pytest.mark.parametrize("expect", [
    ("Hello World")
])
def test_main(expect):
    output = main()
    assert output == expect