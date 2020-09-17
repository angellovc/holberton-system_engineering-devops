#!/usr/bin/python3
""" recurse functions module """
import requests


def recurse(subreddit, hot_list=[], after=''):
    """queries the Reddit API and returns a list of all hot titles
    """
    if isinstance(subreddit, str):
        request = requests.get(
            'https://www.reddit.com/r/{}/hot.json?after={}'.format(subreddit, after),
            headers={'User-agent': 'custom'},
            allow_redirects=False
            )
        if (request.status_code == 200):
            posts = request.json()['data']['children']
            after = request.json()['data']['after']
            for post in posts:
                hot_list.append(post['data']['title'])
            hot_list = recurse(subreddit, hot_list, after)
        else:
            return hot_list
    return None
