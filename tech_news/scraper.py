import time
import requests
import parsel
from tech_news.database import create_news


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
    selector = parsel.Selector(html_content)
    next_page = selector.css("a.next.page-numbers::attr(href)").get()
    if not next_page:
        return None
    return next_page


# Requisito 4
def scrape_noticia(html_content):
    selector = parsel.Selector(html_content)
    url = selector.css("[rel='canonical']::attr(href)").get().strip()
    title = selector.css("h1.entry-title::text").get().strip()
    timestamp = selector.css("li.meta-date::text").get().strip()
    writer = selector.css("a.url.fn.n::text").get()
    comments_count = len(selector.css(".comment-list li").getall())
    summary = "".join(
        selector.css(".entry-content > p:nth-of-type(1) *::text").getall()
        ).strip()
    tags = selector.css(".post-tags a::text").getall()
    category = selector.css("span.label::text").get().strip()

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "comments_count": comments_count,
        "summary": summary,
        "tags": tags,
        "category": category,
    }


# Requisito 5
def get_tech_news(amount):
    base_url = "https://blog.betrybe.com/"
    html_content = fetch(base_url)
    count = 0
    news = []
    while count < amount:
        for url in scrape_novidades(html_content):
            count += 1
            if count > amount:
                break
            else:
                news.append(scrape_noticia(fetch(url)))

        base_url = scrape_next_page_link(html_content)

    create_news(news)
    return news
