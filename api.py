import github_integration


def handle_home() -> str:
    return "Hello World!"


def handle_events(owner_repo, token):
    events = github_integration.fetch_github_events(owner_repo, token)
    return events
