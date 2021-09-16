class News:
    '''
    News class to define news Objects
    '''

    def __init__(self,newsid,name,description,url,category,language,country):
        self.id =newsid
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language
        self.country = country


class Articles:

    all_Articles = []

    def __init__(self, author,name,news_id,title,description,urlToImage,url,publishedAt,content):
        self.news_id =news_id
        self.name = name
        self.author = author  
        self.title = title
        self.description =description
        self.url = url
        self.urlToImage=urlToImage
        self.publishedAt=publishedAt
        self.content=content

    def save_Articles(self):
        Articles.all_Articles.append(self)


    @classmethod
    def clear_Articles(cls):
        Articles.all_Articles.clear()

    @classmethod
    def get_Articles(cls,id):

        response = []

        for review in cls.all_Articles:
            if Articles.news_id == id:
                response.append(Articles)

        return response