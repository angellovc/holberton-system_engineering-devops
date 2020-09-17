#!/usr/bin/python3
""" recurse functions module """
import requests


def recurse(subreddit, hot_list=[], pag=-1):
    """queries the Reddit API and returns a list of all hot titles
    """
    if isinstance(subreddit, str):
        request = requests.get(
            'https://www.reddit.com/r/{}/hot.json?show=all'.format(subreddit),
            headers={'User-agent': 'custom'},
            allow_redirects=False
            )
        if (request.status_code == 200):
            posts = request.json()['data']['children']
            recurse(posts, hot_list, pag + 1)
        else:
            return None
    try:
        hot_list.append(subreddit[pag]['data']['title'])
        hot_list = recurse(subreddit, hot_list, pag + 1)
    except:
        return hot_list
