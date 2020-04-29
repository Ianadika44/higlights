import urllib.request,json
from .models import models


# Article = article.Article
Source = models.Source
Article = models.Article

# Getting api key
api_key = None

# Getting the movie base url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config["NEWS_API_BASE_URL"]


def get_articles(filter):
    '''
    Function that gets the json response to our url request
    '''
    #  get_articles('category=bbc-news')
    get_articles_url = base_url.format('top-headlines',api_key,filter)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        article_results = None

        if get_articles_response['articles']:
            article_results_list = get_articles_response['articles']
            article_results = process_articles(article_results_list)

    return article_results


def process_articles(article_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        movie_list: A list of dictionaries that contain movie details

    Returns :
        movie_results: A list of movie objects
    '''
    article_results = []
    for article_item in article_list:
        source = article_item.get('source')
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')
        content = article_item.get('content')

        if content and  urlToImage:
            article_object = Article(source,author, title, description, url,urlToImage,  publishedAt, content)
            article_results.append(article_object)

    return article_results


def get_sources():
    get_sources_url = base_url.format('sources', api_key,'')

    with urllib.request.urlopen(get_sources_url) as url:
        sources_data = url.read()
        sources_response = json.loads(sources_data)

        sources_object = None
        
        sources_response_data = sources_response['sources']
        if sources_response_data:
            sources_object = process_sources(sources_response_data)

    return sources_object


def process_sources(source_list):
   
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')
        country = source_item.get('country')

        sources_object = Source(id, name, description, url, category,language, country)
        source_results.append(sources_object)

    return source_results
