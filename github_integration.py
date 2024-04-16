import requests


def fetch_github_events(repo_name, access_token):
    url = f"https://api.github.com/repos/{repo_name}/events"
    headers = {"Authorization": f"Bearer {access_token}"}

    try:
        response = requests.get(url, headers=headers)
        events = response.json()
        return events
    except requests.RequestException as e:
        print(f"Error fetching GitHub events: {e}")
        return None
