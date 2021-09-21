import os

# from flask import config
class Config:
    '''
    General configuration parent class
    '''
    ARTICLE_API_BASE_URL ='https://newsapi.org/v2/everything?sources={}&apiKey=55eeed8e67e949608a10479d38e11f96'
    NEWS_SOURCES='https://newsapi.org/v2/sources?apiKey=55eeed8e67e949608a10479d38e11f96'

class ProdConfig(Config):
    '''
    Production configuration child class
    Args:
        Config:The parent configuration class with General configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration child class
    Args:
        Config:The parent configuration class with General configuration settings
    '''
 
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
 }
  
