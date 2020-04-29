import os
class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL ='http://newsapi.org/v2/{}?apiKey={}&{}'
    #   http://newsapi.org/v2/sources?apiKey=asdasdad&
    #   http://newsapi.org/v2/top-headlines?apiKey=asdasdad&sources=bbc-news
    #   http://newsapi.org/v2/top-headlines?apiKey=asdasdad&category=business
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')


class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
} 