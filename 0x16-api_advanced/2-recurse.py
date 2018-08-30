#!/usr/bin/python3
'''
displays top 10 hot posts
'''
import requests


def recurse(subreddit, hot_list=[], after=None):
    user_agent = {'User-agent': 'greg'}
    sub = requests.get('http://www.reddit.com/r/{}/hot.json?after={}'
                       .format(subreddit, after), headers=user_agent)

    try:
        sub = sub.json().get('data')
        after = sub.get('after')
        sub = sub.get('children')
        for obj in sub:
            hot_list.append(obj['data'].get('title'))
        if after is not None:
            recurse(subreddit, hot_list, after)
        return(hot_list)
    except:
        return(None)
