class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL ='http://newsapi.org/v2/{}?apiKey={}&{}'
    #   http://newsapi.org/v2/sources?apiKey=asdasdad&
    #   http://newsapi.org/v2/top-headlines?apiKey=asdasdad&sources=bbc-news
    #   http://newsapi.org/v2/top-headlines?apiKey=asdasdad&category=business



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True