import requests
from typing import List, Dict


GITHUB_SEARCH_API = "https://api.github.com/search/repositories"


class GitHubAPIError(Exception):
    """
    Custom exception for GitHub API Errors.
    """
    pass

def fetch_repositories(created_after: str, limit: int) -> List[Dict]:
    """
    Fetch repositories created after a specific date, sorted by stars.
    """
    query = f"created:>{created_after}"

    params = {
        "q": query,
        "sort": "stars",
        "order": "desc",
        "per_page": min(limit, 100),
    }

    try:
        response = requests.get(GITHUB_SEARCH_API, params=params, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as exc:
        raise GitHubAPIError(f"GitHub API request failed: {exc}")
    

    data = response.json()

    if "items" not in data:
        raise GitHubAPIError("Unexpected API response structure")


    return data["items"][:limit]
