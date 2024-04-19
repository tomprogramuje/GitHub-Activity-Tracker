from api import handle_home, handle_get_events
import pytest


def test_handle_home():
    response = handle_home()

    assert response == "Hello World!"


@pytest.fixture
def token() -> str:
    return "your_access_token"


@pytest.fixture
def mock_fetch_github_events_success(token, monkeypatch):
    mock_events = [
        {"id": 1, "type": "PushEvent", "repo": {"name": "owner/repo"}},
        {"id": 2, "type": "PullRequestEvent", "repo": {"name": "owner/repo"}},
    ]

    def mock_fetch_github_events(repo_name, access_token):
        assert repo_name == "owner/repo"
        assert access_token == token
        return mock_events

    monkeypatch.setattr(
        "github_integration.fetch_github_events", mock_fetch_github_events
    )

    return mock_events


def test_handle_get_events_success(token, mock_fetch_github_events_success):
    events = handle_get_events("owner/repo", token)

    assert events == mock_fetch_github_events_success
