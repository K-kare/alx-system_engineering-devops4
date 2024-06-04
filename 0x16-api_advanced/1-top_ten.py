#!/usr/bin/python3
'''
    this module contains the function top_ten
'''
import requests
from sys import argv


def top_ten(subreddit):
    '''
        returns the top ten posts for a given subreddit
    '''
url = requests.get('https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
headers = {"user-Agent":
}
params = {
"limit" = 10
}
response = requets.get(url, header=headers params=params, allow_redirects=False)
if response.status_code = 404:
print("None")
return
results = response.json().get("data")
[print(c.get('data').get("title"))for c in result.get("children")]
