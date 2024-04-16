import pytest
from api import home


def test_home():
    get = home()

    assert get == "Hello World!"
