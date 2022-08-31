from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    search = search_news({"title": {"$regex": title, "$options": "i"}})
    title_news = []
    for item in search:
        title_news.append((item["title"], item["url"]))
    return title_news


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    search = search_news({'tags': {'$regex': tag, '$options': 'i'}})
    tag_news = []
    for item in search:
        tag_news.append((item['title'], item['url']))
    return tag_news


# Requisito 9
def search_by_category(category):
    search = search_news({'category': {'$regex': category, '$options': 'i'}})
    category_news = []
    for item in search:
        category_news.append((item['title'], item['url']))
    return category_news
