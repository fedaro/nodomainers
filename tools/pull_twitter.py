# -*- coding: utf-8 -*-
import urllib2
from urllib2 import URLError
import json
from dateutil.parser import parse
from nodomainers.database import db
from nodomainers.models import User, Tweet
from configs import *


def get_twitter_req():
    last_id = None
    try:
        last_id = Tweet.query.order_by(Tweet.tweet_id.desc()).first().tweet_id
    except Exception, x:
        pass

    if last_id == None:
        return '%s&%s=%s' % (TWITTER_URL, TWITTER_Q_VAR, TWITTER_QUERY)
    else:
        return '%s&%s=%s&%s=%s' % (TWITTER_URL, TWITTER_OFFSET, last_id, \
                                   TWITTER_Q_VAR, TWITTER_QUERY)


def add_tweet(username, avatar, created_at, text, tweet_id):
    try:
        try:
            u = User(username, avatar)
            db.session.add(u)
        except Exception, x:
            print "Unhandled exception adding user:" + str(x)
        try:
            t = Tweet(u, text, created_at, tweet_id)
            db.session.add(t)
        except Exception, x:
            print "Unhandled exception adding tweet:" + str(x)
        db.session.commit()
    except Exception, x:
        print "Unhandled Exception: " + str(x)


def parse_result(one_result):
    username = None
    text = None
    created_at = None
    if u'from_user' in one_result:
        username = one_result[u'from_user']
    if u'text' in one_result:
        text = one_result[u'text']
    if u'created_at' in one_result:
        created_at_str = one_result[u'created_at']
    try:
        created_at = parse(created_at_str)
    except Exception, x:
        print "Could not convert date to datetime: " + str(x)
        return
    if u'profile_image_url' in one_result:
        avatar = one_result[u'profile_image_url']
    if u'id' in one_result:
        tweet_id = one_result[u'id']
    if username and text and created_at and avatar and tweet_id:
        add_tweet(username, avatar, created_at, text, tweet_id)


def decode_json(file_resp):
    try:
        decoded = json.load(file_resp)
        map(parse_result, decoded[u'results'])
    except Exception, x:
        print "Unhandled exception: " + str(x)

try:
    request = get_twitter_req()
    f = urllib2.urlopen(request)
    decode_json(f)
except URLError, x:
    print "URLError: " + str(x)
except Exception, x:
    print "Unhandled error: " + str(x)
