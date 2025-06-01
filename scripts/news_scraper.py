import requests
from bs4 import BeautifulSoup

def fetch_news():
    url = "https://news.yahoo.co.jp/topics/world"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    res = requests.get(url, headers=headers)
    if res.status_code != 200:
        print(f"Error fetching news: {res.status_code}")
        return []

    soup = BeautifulSoup(res.text, "html.parser")
    articles = []

    # ページ内のすべてのリンクから記事タイトルとURLを取得（試験的）
    for a_tag in soup.find_all("a", href=True):
        title = a_tag.get_text(strip=True)
        href = a_tag['href']
        if title and href.startswith("https://news.yahoo.co.jp/articles/"):
            content = fetch_article_body(href)
            articles.append({"title": title, "content": content})
        if len(articles) >= 5:
            break

    return articles

def fetch_article_body(article_url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    res = requests.get(article_url, headers=headers)
    if res.status_code != 200:
        return ""

    soup = BeautifulSoup(res.text, "html.parser")
    paragraphs = soup.select("article p")
    if not paragraphs:
        # Yahoo の記事でない場合のバックアップ
        paragraphs = soup.find_all("p")

    content = "\n".join(p.get_text(strip=True) for p in paragraphs)
    return content