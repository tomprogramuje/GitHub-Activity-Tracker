from dataclasses import dataclass
import json
import datetime


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
            created_at=datetime.datetime.fromisoformat(item["created_at"]),
        )
        events.append(event)

    return events


def get_statistics(json_file):
    events = parse_json(json_file)

    delete_events = [event.created_at for event in events if event.type == "DeleteEvent"]
    delete_events.reverse()

    time_diffs = [delete_events[i + 1] - delete_events[i] for i in range(len(delete_events) - 1)]
    total_time_diff = sum(time_diffs, datetime.timedelta())
    average_time_diff = total_time_diff / len(time_diffs)

    return average_time_diff
