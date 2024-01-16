#!/usr/bin/python3
"""Function that prints top ten hot posts for a given subreddit"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Gets hot posts in subreddit
       Args:
           subreddit (str): name of subreddit
           hot_list (list): list of titles
           after (str): id of next set of results
    """
    url = 'https://api.reddit.com/r/'
    headers = {'User-Agent': 'my-app/0.0.1'}
    params = {"after": after} if after else {}
    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()["data"]
        hot_list += [post["data"]["title"] for post in data["children"]]
        after = data["after"]
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None
