from api import handle_home


def test_handle_home():
    response = handle_home()

    assert response == "Hello World!"
