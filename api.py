import github_integration


def handle_home() -> str:
    return "Hello World!"


def handle_get_events(repo_name, access_token):
    events = github_integration.fetch_github_events(repo_name, access_token)
    return events
