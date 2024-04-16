import pytest
from api import handle_home


def test_handle_home():
    get = handle_home()

    assert get == "Hello World!"
