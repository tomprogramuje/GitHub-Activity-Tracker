import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "Hello World!"}


@pytest.fixture
def mock_repo_name() -> str:
    return "owner/repo"


@pytest.fixture
def token() -> str:
    return "your_access_token"


@pytest.fixture
def mock_handle_get_events_success(mock_repo_name, token, monkeypatch):
    mock_events = [
        {"id": 1, "type": "PushEvent", "repo": {"name": "owner/repo"}},
        {"id": 2, "type": "PullRequestEvent", "repo": {"name": "owner/repo"}},
    ]

    def mock_handle_get_events(repo_name, access_token):
        assert repo_name == mock_repo_name
        assert access_token == token

        return mock_events

    monkeypatch.setattr("api.handle_get_events", mock_handle_get_events)

    return mock_events


def test_get_events_success(mock_repo_name, token, mock_handle_get_events_success):
    params = {"repo_name": mock_repo_name, "access_token": token}
    response = client.get(f"/events", params=params)

    assert response.status_code == 200
    assert response.json() == mock_handle_get_events_success
