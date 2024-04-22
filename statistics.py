from dataclasses import dataclass
import json
from datetime import datetime


@dataclass
class GitHubEvent:
    id: str
    type: str
    repo_name: str
    created_at: datetime


def parse_json(json_file):
    with open(json_file) as json_file:
        data = json.load(json_file)

    events = []
    for item in data:
        event = GitHubEvent(
            id=item["id"],
            type=item["type"],
            repo_name=item["repo"]["name"],
            created_at=datetime.fromisoformat(item["created_at"]),
        )
        events.append(event)

    print(events)


parse_json("sample.json")
