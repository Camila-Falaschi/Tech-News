from parsel import Selector
import requests
import time


# Requisito 1
def fetch(url):
    HEADERS = {"user-agent": "Fake user-agent"}

    try:
        response = requests.get(url, headers=HEADERS, timeout=3)
        response.raise_for_status()
        time.sleep(1)
    except (requests.HTTPError, requests.ReadTimeout):
        return None

    return response.text


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(html_content)
    urls = []

    for url in selector.css("h2.entry-title"):
        href = url.css("a::attr(href)").get()
        urls.append(href)

    return urls


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    next_page_url = selector.css("div.nav-links > a.next::attr(href)").get()

    return next_page_url


# Requisito 4
def scrape_news(html_content):
    selector = Selector(html_content)
    page_url = selector.css("head > link[rel*=canonical]::attr(href)").get()
    title = selector.css("h1.entry-title::text").get()
    timestamp = selector.css("ul.post-meta > li:nth-child(2)::text").get()
    writer = selector.css("span.author > a::text").get()
    reading_time = selector.css("li.meta-reading-time::text").get()
    summary_list = selector.css(
        "div.entry-content > p:first-of-type *::text"
    ).getall()
    summary = ""
    for phrase in summary_list:
        summary += phrase

    category = selector.css("a.category-style > span.label::text").get()

    return {
        "url": page_url,
        "title": title.strip(),
        "timestamp": timestamp,
        "writer": writer,
        "reading_time": int(reading_time.split()[0]),
        "summary": summary.strip(),
        "category": category,
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
