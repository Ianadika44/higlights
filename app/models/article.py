class Article:
    '''
    Movie class to define Movie Objects
    '''

    def __init__(self,id,name,author,title,description,url,publishedAt,content):
        self.id =id
        self.name=name
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.publishedAt = publishedAt
        self.content = content