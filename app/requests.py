import urllib.request,json
from .models import  News

#....

import urllib.request,json
from .models import News

# Getting api key
api_key= None
# Getting the news article api key
article_url= None
# Getting the secret key
secret_key = None
# Getting the source apikey
source_api = None

def configure_request(app):
   global api_key, article_url ,secret_key,source_api
   secret_key = app.config['SECRET_KEY']
   article_url = app.config['NEWS_ARTICLE_API']
   source_api = app.config['NEWS_SOURCE_API']
   api_key = app.config['API_KEY']

def get_sources():
   '''
   view sourcegen
   '''
   get_sourcegen_url = source_api 
   print('...........')
   print(get_sourcegen_url)
   print('...........')

   with urllib.request.urlopen(get_sourcegen_url) as url:
      get_source_data = url.read()
      get_source_response = json.loads(get_source_data)

      sourcegen_results = None

      if get_source_response['sources']:
         sourcegen_list = get_source_response['sources']
         sourcegen_results = process_source(sourcegen_list)

   return sourcegen_results

def process_source(sourcegen_list):
   '''
   views news results transforming them to a list objects
   
   Arg:
   sourcegen_list: a dictionary list of news details

   Return:
   sourcegen_results: gives list feedback of news

   '''

   sourcegen_results = []
   for sourcegen_item in sourcegen_list:
      id = sourcegen_item.get('id')
      name = sourcegen_item.get('name')
      description = sourcegen_item.get('description')
      url = sourcegen_item.get('url')
      category = sourcegen_item.get('category')
      language = sourcegen_item.get('language')
      country = sourcegen_item.get('country')

   if url:
    news_object = News(id,name,url,category,language,country) 
    sourcegen_results.append(news_object)

   return sourcegen_results


#....