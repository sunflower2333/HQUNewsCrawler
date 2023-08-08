from flask import Flask

app = Flask(__name__)


class Page:
    def __init__(self, url):
        self.url = url
        self.title = None
        self.time = None
        self.resources = []

    def find_contents_by_class_name(self, class_name):
        return


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>" \
           "<a href=\"/hdxw\">Click Here to visit HQU news.</a>"


@app.route("/hdxw")
def news_main():
    target_url = 'https://news.hqu.edu.cn/hdyw.htm'
    page_num = 0
    page = "<p>nothing here currently<p>"

    # Request the target news website.
    web_contents = request_web(target_url, page_num)

    # Parse the web and get url list to news page.
    news_url_list = get_news_url_list(web_contents)

    # Parse each news page and get contents object list.

    for page in news_url_list:
        parse_single_news_page()

    # Generate our page by what contents we get.
    # Return html to display in web browser.
    return generate_page(news)


def request_web(url, page_name):
    contents = ""
    return contents


def get_news_url_list(contents):
    news_list = []
    return news_list


def parse_single_news_page(url):
    return


def generate_page(news_list):
    return
