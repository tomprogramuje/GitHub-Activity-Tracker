from dataclasses import dataclass
import pytest
from github_integration import fetch_github_events


@dataclass
class MockResponse:
    json_data: dict | None
    status_code: int
    text: str = ""

    def json(self):
        return self.json_data


@pytest.fixture
def mock_requests_get_success(monkeypatch):
    def mock_get(*args, **kwargs):
        mock_response = MockResponse(
            {"id": 1, "type": "PullRequestEvent", "repo": {"name": "owner/repo1"}}, 200
        )
        return mock_response

    monkeypatch.setattr("requests.get", mock_get)

def test_fetch_github_events_success(mock_requests_get_success):
    events = fetch_github_events("owner/repo1", "your_access_token")

    assert len(events) == 3
    assert events["type"] == "PullRequestEvent"
