#!/usr/bin/python3
'''
displays top 10 hot posts
'''
import requests


def top_ten(subreddit):
    user_agent = {'User-agent': 'greg'}
    sub = requests.get('http://www.reddit.com/r/{}/hot.json'
                       .format(subreddit), headers=user_agent)

    try:
        sub = sub.json().get('data')
        sub = sub.get('children')
        i = 0
        for obj in sub:
            if i > 9:
                break
            print(obj['data'].get('title'))
            i += 1

    except:
        print('None')
