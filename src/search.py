
# search/tweetsの場合は1回のリクエストで100ツイートまで
# 15分ごとに180回までリクエストが可能
# 一度に取得できるツイート数は最大18000
# https://qiita.com/mpyw/items/32d44a063389236c0a65
# API日本語訳
# http://westplain.sakuraweb.com/translate/twitter/Documentation/REST-APIs/Public-API/REST-APIs.cgi

import urllib
from requests_oauthlib import OAuth1
import requests
import datetime
from dateutil import tz
import sys

def search_tweets(CK, CKS, AT, ATS, word, count, range, since):
    # 文字列設定
    word += ' exclude:retweets' # RTは除く
    word = urllib.parse.quote_plus(word)
    dt_now = datetime.datetime.utcnow()
    dt_now_5 = dt_now + datetime.timedelta(minutes=since)
    # リクエスト
    url = "https://api.twitter.com/1.1/search/tweets.json?lang=ja&q="+word+"&count="+str(count)
    auth = OAuth1(CK, CKS, AT, ATS)
    response = requests.get(url, auth=auth)
    data = response.json()
    if not 'statuses' in data:
        print(data)# {'errors': [{'message': 'Rate limit exceeded', 'code': 88}]}
        sys.exit() # あるいはちゃんとSleepする
    data = data['statuses']
    # 2回目以降のリクエスト
    cnt = 0
    tweets = []
    while True:
        if len(data) == 0:
            break
        cnt += 1
        if cnt > range:
            break
        for tweet in data:
            tweet_time = tweet['created_at'].split()
            temp_str = date_tf(tweet_time[1])
            tweet_time = datetime.datetime.strptime(tweet_time[5] + '-' + temp_str + '-' + tweet_time[2] + ' ' + tweet_time[3], '%Y-%m-%d %H:%M:%S')
            if dt_now_5 < tweet_time:
                temp_str_tweet = str(tweet_time) + '\n' + tweet['text']
                tweets.append(temp_str_tweet)
            maxid = int(tweet['id']) - 1
        url = "https://api.twitter.com/1.1/search/tweets.json?lang=ja&q="+word+"&count="+str(count)+"&max_id="+str(maxid)
        response = requests.get(url, auth=auth)
        try:
            data = response.json()
            if not 'statuses' in data:
                print(data)# {'errors': [{'message': 'Rate limit exceeded', 'code': 88}]}
                sys.exit() # あるいはちゃんとSleepする
            data = data['statuses']
        except KeyError: # リクエスト回数が上限に達した場合のデータのエラー処理
            print('上限まで検索しました')
            break
    return tweets


def date_tf(s):
    if s == 'Jan':
        return '01'
    elif s == 'Feb':
        return '02'
    elif s == 'Mar':
        return '03' 
    elif s == 'Apr':
        return '04' 
    elif s == 'May':
        return '05' 
    elif s == 'Jun':
        return '06' 
    elif s == 'Jul':
        return '07' 
    elif s == 'Aug':
        return '08' 
    elif s == 'Sep':
        return '09' 
    elif s == 'Oct':
        return '10' 
    elif s == 'Nov':
        return '11' 
    elif s == 'Dec':
        return '12'
    else:
        print('月エラー') 
        sys.exit()


