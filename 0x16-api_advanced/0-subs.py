#!/usr/bin/python3
"""
number in subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """
    Function to retrieve the number of subscribers for a given subreddit.
    Returns int: The number of subscribers for the specified subreddit.
    """
    url = 'https://www.reddit.com'
    header = {
        'Accept': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }

    """Make the request to fetch subreddit information"""
    response = requests.get('{}/r/{}/about/.json'.format(url, subreddit),
                            headers=header,
                            allow_redirects=False
                            )

    """Check if the response is successful (status code 200)"""
    if response.status_code == 200:
        return response.json()['data']['subscribers']
    """
    Return 0 if the subreddit does not exist or an error occurs
    """
    return 0
