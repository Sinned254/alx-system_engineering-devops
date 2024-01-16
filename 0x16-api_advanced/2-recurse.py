#!/usr/bin/python3
import requests


def recurse(subreddit, hot_list=[], after=None):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0;"
               "Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
               "Chrome/58.0.3029.110 Safari/537.3"}
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
