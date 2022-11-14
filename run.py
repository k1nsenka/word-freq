from src import auth, search


def main():
    # APIの秘密鍵
    # CK:コンシューマーキー
    # CKS:コンシューマーシークレット
    # AT:アクセストークン
    # ATS:アクセストークンシークレット
    CK, CKS, AT, ATS = auth.auth_keys('key/keys.txt')
    # 検索時のパラメーター
    word = '別れました ありがとう' # 検索ワード
    count = 100 # 一回あたりの検索数(最大100/デフォルトは15)
    range = 5 # 検索回数の上限値(最大180/15分でリセット)
    # ツイート検索・テキストの抽出
    tweets = search.search_tweets(CK, CKS, AT, ATS, word, count, range)
    # 検索結果を表示
    print(tweets[0:4])



if __name__ == '__main__':
    main()