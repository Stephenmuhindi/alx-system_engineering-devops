import requests

def number_of_subscribers(subreddit):
    """
    Fetches the number of subscribers for a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit.
        
    Returns:
        int: The number of subscribers. Returns 0 if the subreddit does not exist or an error occurs.
    """
    url = f'https://www.reddit.com/r/{subreddit}/about/.json'
    headers = {
        'Accept': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
        return response.json().get('data', {}).get('subscribers', 0)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return 0

