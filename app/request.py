from app import app
import urllib.request
import json
from .models import article,source

Article = article.Article
Source = source.Source

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the movie base url
base_url = app.config["NEWS_API_BASE_URL"]


def get_articles(category):
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url = base_url.format(category, api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        article_results = None

        if get_articles_response['articles']:
            article_results_list = get_articles_response['articles']
            article_results = process_articles(article_results_list)

    return article_results


def process_results(article_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        movie_list: A list of dictionaries that contain movie details

    Returns :
        movie_results: A list of movie objects
    '''
    article_results = []
    for article_item in article_list:
        id = article_item.get('id')
        name = article_item.get('name')
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        publishedAt = article_item.get('publishedAt')
        content = article_item.get('content')

        if content:
            article_object = Article(
                id, name, author, title, description, url, publishedAt, content)
            article_results.append(article_object)

    return article_results


def get_source(id):
    get_source_details_url = base_url.format(id, api_key)

    with urllib.request.urlopen(get_source_details_url) as url:
        source_details_data = url.read()
        source_details_response = json.loads(source_details_data)

        source_object = None
        if source_details_response:
            id = source_item.get('id')
            name = source_item.get('name')
            description = source_item.get('description')
            url = source_item.get('url')
            category = source_item.get('category')
            language = source_item.get('language')
            country = source_item.get('country')

            source_object = Source(id, name, description,
                                   url, category, language, country)

    return movie_object


def process_results(source_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects
General_news = get_sources()

    Args:
        movie_list: A list of dictionaries that contain movie details

    Returns :
        movie_results: A list of movie objects
    '''
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')
        country = source_item.get('country')

        if name:
            sources_object = Source(id, name, description, url, category, country)
            sources_results.append(sources_object)

    return source_results
