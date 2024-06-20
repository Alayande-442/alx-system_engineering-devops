#!/usr/bin/python3

import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.
    If an invalid subreddit is given, the function should return 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "ALX-Subscriber-Count-Agent"
    }
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except Exception:
        return 0

# Example usage (this part should not be included in the final submission file):
if __name__ == "__main__":
    subreddit = "python"
    print(f"The number of subscribers in r/{subreddit} is {number_of_subscribers(subreddit)}")

