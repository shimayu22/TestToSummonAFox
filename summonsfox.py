# coding: utf-8
# Your code here!
import requests
from bs4 import BeautifulSoup

def get_fox_infomation():
    # アクセスするURL
    url = "http://fox-info.net/fox-gallery"
    html = requests.get(url)

    # HTMLパース用のオブジェクトを作成する
    soup = BeautifulSoup(html.text, 'html.parser')

    # 最初のdt要素を抽出する
    # ページの記事配置自体がランダムなので、単純に開いて一つ目の記事を取得する
    dt = soup.find("dt",attrs={"class","gallery-icon landscape"})

    # a要素を抽出する
    a = dt.find("a")
    
    # URLを取得する
    link = a.get("href")

    # 画像を取得する
    img = dt.find("img")
    src = img.get("src")

    # 記事のタイトルを取得する
    article_html = requests.get(link)

    # HTMLパース用のオブジェクトを作成する
    article_soup = BeautifulSoup(article_html.text, 'html.parser')

    # title要素を抽出する
    title = article_soup.title

    # 記事タイトルを整形して取得する
    shaping_title = title.string.split(" ")

    return shaping_title[0],link,src

def check_fox_call(summons_line):
    fox_cry_list = ["こーん","こん","コーン","コン"]

    for fox_cry in fox_cry_list:
        if fox_cry in summons_line:
            return True
    return False    

summons_line = input("狐を召喚してください：")

if check_fox_call(summons_line):
    title_text,url,image_url = get_fox_infomation()
    print(title_text)
    print(url)
    print(image_url)
else:
    print("狐語でおｋ")
