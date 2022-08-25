import time
import requests
import parsel


# Requisito 1
def fetch(url, timeout=3):
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        time.sleep(1)
    except (requests.HTTPError, requests.ReadTimeout):
        return None
    else:
        return requests.get(url).text


# Requisito 2
def scrape_novidades(html_content):
    selector = parsel.Selector(html_content)
    news = selector.css("a.cs-overlay-link::attr(href)").getall()
    if not news:
        return []
    return news


# page_content = fetch("https://blog.betrybe.com")


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
