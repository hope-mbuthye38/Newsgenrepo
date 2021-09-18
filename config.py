import os

class Config:

    SECRET_KEY ='5578890022345789'
    NEWS_ARTICLE_API='https://newsapi.org/v2/everything?source={}&apiKey=55eeed8e67e949608a10479d38e11f96'
    API_KEY ='55eeed8e67e949608a10479d38e11f96'
    NEWS_SOURCE_API ='https://newsapi.org/v2/sources?apiKey=55eeed8e67e949608a10479d38e11f96'


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}