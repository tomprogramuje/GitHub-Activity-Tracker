import requests

token = "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"


def fetch_github_events(repo_name, access_token):
    url = f"https://api.github.com/repos/{repo_name}/events"
    headers = {"Authorization": f"Bearer {access_token}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        events = response.json()
        return events
    except requests.RequestException as e:
        raise requests.HTTPError(f"HTTP Error {e}")
