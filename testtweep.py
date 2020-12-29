#! /usr/bin/python
import os.path
import tweepy
from keys import keys

SCREEN_NAME = keys['screen_name']
CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

gamers = []

if not os.path.isfile("followers.txt"):
    f = open("followers.txt","w")
    for i in gamers:
        f.write(i+"\n")
    f.close()
else:
    f = open("followers.txt","r")
    for i in f.readlines():
        gamers.append(i.replace('\n',''))
    f.close()
    print(gamers)
    
followers = api.followers_ids(SCREEN_NAME)
friends = api.friends_ids(SCREEN_NAME)
ff = open("followers.txt","a")
for f in friends:
    if f not in followers:
        u = api.get_user(f)
        if(u.screen_name not in gamers):
            print(u.screen_name)
            ff.write(u.screen_name+"\n")
        # api.destroy_friendship(f)
ff.close()
