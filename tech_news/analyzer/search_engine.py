from tech_news.database import search_news
from datetime import date as dt


# Requisito 6
# https://www.thecodebuzz.com/mongodb-query-case-sensitive-case-insensitive/
def search_by_title(title):
    search = search_news({"title": {"$regex": title, "$options": "i"}})
    title_news = []
    for item in search:
        if len(search) > 0:
            title_news.append((item["title"], item["url"]))
        else:
            title_news = []
    return title_news


# Requisito 7
# https://docs.python.org/3/library/datetime.html
# https://www.hashtagtreinamentos.com/como-trabalhar-com-tempo-no-python?gclid=CjwKCAjw6raYBhB7EiwABge5Klo1AKnZoJMo1a_zb-fE8BhnxIgCyY26-YFcSpFW_SUhFP40fb-y4BoCLTEQAvD_BwE
def search_by_date(date):
    try:
        date_iso = dt.fromisoformat(date)
        date_string = dt.strftime(date_iso, "%d/%m/%Y")
        search = search_news({"timestamp": date_string})
        date_news = []
        for item in search:
            if len(search) > 0:
                date_news.append((item["title"], item["url"]))
            else:
                date_news = []
        return date_news
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    search = search_news({'tags': {'$regex': tag, '$options': 'i'}})
    tag_news = []
    for item in search:
        if len(search) > 0:
            tag_news.append((item["title"], item["url"]))
        else:
            tag_news = []
    return tag_news


# Requisito 9
def search_by_category(category):
    search = search_news({'category': {'$regex': category, '$options': 'i'}})
    category_news = []
    for item in search:
        if len(search) > 0:
            category_news.append((item['title'], item['url']))
        else:
            category_news = []
    return category_news
