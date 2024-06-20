#!/usr/bin/python3
"""
A recursive function thatt queries the Reddit API and returns a list containing
the titles of all articles for a given subreddit. Function to return None if no
results are found for the given subreddit
"""
import requests
import sys

def add_title(hot_list, hot_posts):
    """ Adds items to a list """
    if len(hot_posts) == 0:
        return
    hot_list.append(hot_posts[0]['data']['title'])
    hot_posts.pop(0)
    add_title(hot_list, hot_posts)


def recurse(subreddit, hot_list=[], after=None):
    """ Querries to a Reddit API """
    headers = {'User-Agent': 'Mozilla/5.0'}

    params = {
            'after': after
            }

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url,
            headers=headers,
            params=params,
            allow_redirects=False)

    if response.status_code != 200:
        return None

    dic = response.json()
    hot_posts = dic['data']['children']
    add_title(hot_list, hot_posts)
    after = dic['data']['after']
    if not after:
        return hot_list
    return recurse(subreddit, hot_list=hot_list, after=after)
