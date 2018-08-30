#!/usr/bin/python3
'''
returns number of subscribers for a given subreddit
'''
import requests
user_agent = {'User-agent': 'greg'}

def number_of_subscribers(subreddit):
    sub = requests.get('http://www.reddit.com/r/{}/about.json'.format(subreddit), headers = user_agent)
    if not sub:
        return(0)
    sub = sub.json().get('data')
    for k, v in sub.items():
        if k == 'subscribers':
            return(v)

