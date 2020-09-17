#!/usr/bin/python3
""" Reddit api query script """
import requests
from sys import argv


def number_of_subscribers(subreddit):
    """ queries the Reddit API and returns the
    number of subscribers for a given subreddit
    """
    request = requests.get(
        'https://www.reddit.com/r/{}/about.json'.format(subreddit),
        headers={'User-agent': 'custom'}
    )
    return request.json()['data']['subscribers']
