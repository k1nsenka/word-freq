
# search/tweetsの場合は1回のリクエストで100ツイートまで
# 15分ごとに180回までリクエストが可能
# 一度に取得できるツイート数は最大18000
# https://qiita.com/mpyw/items/32d44a063389236c0a65
# API日本語訳
# http://westplain.sakuraweb.com/translate/twitter/Documentation/REST-APIs/Public-API/REST-APIs.cgi

import urllib
from requests_oauthlib import OAuth1
import requests
import sys

def search_tweets(CK, CKS, AT, ATS, word, count, range):
    # 文字列設定
    word += ' exclude:retweets' # RTは除く
    word = urllib.parse.quote_plus(word)
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
            tweets.append(tweet['text'])
            maxid = int(tweet["id"]) - 1
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


