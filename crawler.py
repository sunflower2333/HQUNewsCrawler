from flask import Flask
from bs4 import BeautifulSoup
import requests as rqs

app = Flask(__name__)
TARGET_URL = 'https://news.hqu.edu.cn/hdyw.htm'


class News:
    def __init__(self, new_info):
        self.time = new_info.find('span').string[1:-1]
        self.title = new_info.find('a').string
        self.url = TARGET_URL + "/../" + new_info.find('a')['href']
        # parts = BeautifulSoup(rqs.request(self.url).text).find('v_news_content')


@app.route("/")
def hello_world():
    return """
    <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>hdxw</title>
        </head>
        <body>
            <a href="./hdxw">这是华大新闻的站点</a>
        </body>
    </html>
   """


@app.route("/hdxw")
def news_main():
    page_num = 0

    # Request the target news website.
    web_contents = request_web(TARGET_URL, page_num)

    # Parse the web and get url list to news page.
    news_list = get_news_list(web_contents)

    # Generate our page by what contents we get.
    # Return html to display in web browser.
    return generate_page(news_list)


def request_web(url, page_num=0):
    ua = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 12; MI 5) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/110.0.0.0 Mobile Safari/537.36 EdgA/110.0.1587.66'}

    # TODO Add pages support.
    response = rqs.get(url, headers=ua)
    response.encoding = 'UTF-8'
    return response.text


def get_news_list(contents):
    news = []
    bs = BeautifulSoup(contents, "html.parser")
    news_lists_div = bs.find_all("div", class_="Newslist")
    for news_list in news_lists_div:
        news_info = news_list.find_all('li')
        for i in news_info:
            news.append(News(i))
    return news


def generate_page(news_list):
    page = """
        <html>
            <head>
                <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
            </head>
            <p>华大要闻 Page 1 <p>
            <ul>
                %s
            <ul>
        </html>
    """

    new_entry = """
            <li>
                <a href="%s">%s</a>
            </li>
    """
    new_entries = ""
    for i in news_list:
        new_entries += new_entry % (i.url, i.title, i.time)
    return page % new_entries
