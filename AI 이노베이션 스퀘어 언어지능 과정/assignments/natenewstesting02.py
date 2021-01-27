from newspaper import Article
from bs4 import BeautifulSoup
import requests

def download(url, params={}, retries=3):
    resp = None

    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36"}

    try:
        resp = requests.get(url, params=params, headers=header)
        resp.raise_for_status()
    except requests.exceptions.HTTPError as e:
        if 500 <= e.response.status_code < 600 and retries > 0:
            print(retries)
            resp = download(url, params, retries - 1)
        else:
            print(e.response.status_code)
            print(e.response.reason)
            print(e.request.headers)

    return resp

html = download("https://news.nate.com/column")
natenews = BeautifulSoup(html.text, "lxml")

natenewstitellists = natenews.select("div[id=newsContents] > div > div > div > ul > li > a")
# cid706693 > div > div > div > a

k = []
t = 10

for links in natenewstitellists:
    l = links.get('href')
    k.append('https:' + l)

# print(k)
for i in range(0, 150):
    url = k[i]
    a = Article(url, language='ko')
    a.download()
    a.parse()
    with open( "%d.txt" % int(i + t), "w", encoding="utf-8") as f:
        f.write(a.title)
        f.write(a.text)
        f.close()

# cid706693 > div > div > div > a
# cid706693 > div > div > ul > li:nth-child(1) > a
