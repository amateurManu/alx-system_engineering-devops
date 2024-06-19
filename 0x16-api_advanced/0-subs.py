#!/usr/bin/python3
"""
Function that queries the Reddit API and returns number of subscribers
(not active users, total subscribers) for a given subredit.
"""
import requests
import sys

def number_of_subscribers(subreddit):
    """ Querries to Reddit API """
    u_agent = 'Mozilla/5.0'

    headers = {
            'User-agent': u_agent
            }

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    data = response.json()
    if 'data' not in data:
        return 0
    if 'subscribers' not in data.get('data'):
        return 0
    return response.json()['data']['subscribers']
