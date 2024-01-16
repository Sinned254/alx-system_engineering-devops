#!/usr/bin/python3
"""Function that prints top ten hot posts for a given subreddit"""
import requests


def top_ten(subreddit):
    """Gets top ten posts in subreddit
       Args:
           subreddit (str): name of subreddit
    """
    url = 'https://api.reddit.com/r/'
    headers = {'User-Agent': 'my-app/0.0.1'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        for post in response.json()["data"]["children"]:
            print(post["data"]["title"])
    else:
        print(None)
