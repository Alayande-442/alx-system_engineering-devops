#!/usr/bin/python3

import requests

def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers for a given subreddit."""
    # Define the URL for the subreddit
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # Define the headers, including a custom User-Agent
    headers = {
        "User-Agent": "ALX-Subscriber-Count-Agent"
    }
    
    try:
        # Make a GET request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            # Return the number of subscribers
            return data['data']['subscribers']
        else:
            # If the subreddit is invalid or any other error occurs, return 0
            return 0
    except Exception as e:
        # In case of any exception, return 0
        return 0

# Example usage:
if __name__ == "__main__":
    subreddit = "python"
    print(f"The number of subscribers in r/{subreddit} is {number_of_subscribers(subreddit)}")

