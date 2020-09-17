#!/usr/bin/python3
""" top_ten functions module """
import requests
from sys import argv
import json


def top_ten(subreddit):
    """queries the Reddit API and prints the titles of the
    first 10 hot posts listed for a given subreddit
    """
    request = requests.get(
        'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit),
        headers={'User-agent': 'custom'},
        allow_redirects=False
    )
    if (request.status_code == 200):
        posts = request.json()['data']['children']
        for post in posts:
            print(post['data']['title'])
    else:
        print(None)
