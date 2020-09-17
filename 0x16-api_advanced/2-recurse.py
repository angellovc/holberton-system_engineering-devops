#!/usr/bin/python3
""" recurse functions module """
import requests


def recurse(subreddit, hot_list=[]):
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
            recurse(posts, hot_list)
        else:
            return None
    try:
        pag = len(hot_list)
        hot_list.append(subreddit[pag]['data']['title'])
        hot_list = recurse(subreddit, hot_list)
    except:
        return hot_list
