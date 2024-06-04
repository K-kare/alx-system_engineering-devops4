#!/usr/bin/python3
"""
function returns the number of subscribers for a given subreddit
"""
import requests

def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code == 200:
        data = r.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0

