import gnp

def get_news(query):
    content =gnp.get_google_news_query(query)
    return content['stories'][:10]


