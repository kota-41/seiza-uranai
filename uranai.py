import requests
from bs4 import BeautifulSoup

target_url = 'https://www.asahi.com/uranai/12seiza/'
# リンクにアクセス
response = requests.get(target_url)
# htmlを取得
soup = BeautifulSoup(response.content, 'html.parser')
yotei = soup.find("ol", class_="UranaiRank")
a_tags = yotei.find_all('a')
count = 0
word = ""
# aタグを取得
for a_tag in a_tags:

    href = a_tag.text

    if "座" in href:

        count = count + 1

        word = str(word) + f"{count}位 : {href}\n"

    elif href == "詳しく":

        href = a_tag.get('href')

        href = "https://www.asahi.com" + str(href)

        word = str(word) + f"詳しく : {href}\n"

print(word)
