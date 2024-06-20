#!/usr/bin/python3
"""
Function that queries the Reddit API and prints the titles of the first
10 hot spots for a given subreddit

Prints None if not a valid subreddit and handles redirects when encountering
an invalid subreddit
"""
import requests
import sys


def top_ten(subreddit):
    """ Querries to Reddit API """
    headers = {'User-Agent': 'Mozilla/5.0'}

    params = {
            'limit': 10
            }

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url,
            headers=headers,
            params=params,
            allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return
    dic = response.json()
    hot_posts = dic['data']['children']
    if len(hot_posts) == 0:
        print(None)
    else:
        for post in hot_posts:
            print(post['data']['title'])
