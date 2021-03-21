import requests
from bs4 import BeautifulSoup
import pandas as pd


def to_csv_yahoo():
    # yahoo!ニュースのレスポンス取得
    response = requests.get('https://news.yahoo.co.jp')

    # BeautifulSoupを作成
    html = BeautifulSoup(response.content, 'html.parser')

    df = pd.DataFrame(columns=['pickup', 'url'])

    # トピックスを抽出
    i = 0
    for a in html.select('#uamods-topics div div div ul li a'):
        # 出力処理
        df.loc[i] = [list(a.strings)[0], a.get('href')]
        i += 1

    df.to_csv("yahoo.csv", index=False)


if __name__ == '__main__':
    to_csv_yahoo()
