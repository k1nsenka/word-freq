from src import auth, search


def main():
    # APIの秘密鍵
    # CK:コンシューマーキー
    # CKS:コンシューマーシークレット
    # AT:アクセストークン
    # ATS:アクセストークンシークレット
    CK, CKS, AT, ATS = auth.auth_keys('key/keys.txt')
    # 検索時のパラメーター
    word = 'ビットコイン' # 検索ワード
    count = 100 # 一回あたりの検索数(最大100/デフォルトは15)
    range = 5 # 検索回数の上限値(最大180/15分でリセット)
    since = -5 # 何分前（マイナス)までのツイートを探すか
    # ツイート検索・テキストの抽出
    tweets = search.search_tweets(CK, CKS, AT, ATS, word, count, range, since)
    # 検索結果を表示
    with open('./key/tweets.txt', 'w') as f:
        for d in tweets:
            f.write(str(tweets.index(d)) + "#######################################\n")
            f.write("%s\n" % d)
        print('風速： ', end="")
        print(len(tweets)/abs(since), end="")
        print(' [tweets/min]\n')


if __name__ == '__main__':
    main()