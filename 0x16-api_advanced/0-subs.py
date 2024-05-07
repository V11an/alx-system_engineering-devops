#!/usr/bin/python3
"""Function used to query subscribers on given Reddit subreddit."""

import requests


def number_of_subscribers(subreddit):
    """Return total number of subscribers on given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "vllan.agent:v1.0.0 (by /u/vllan)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
