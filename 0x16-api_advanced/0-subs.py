#!/usr/bin/python3
"""
number in subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
    Fetches the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
    """
    url = f'https://www.reddit.com/r/{subreddit}/about/.json'
    headers = {
            'Accept': 'application/json',
            'User-Agent': 'reddituser'
            }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()
        return response.json().get('data', {}).get('subscribers', 0)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return 0
