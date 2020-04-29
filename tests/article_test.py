import unittest
from app.models import article
Article = article.Article


class ArticleTest(unittest.TestCase):
    
    def setUp(self):
        

        self.new_article = Article('','','','','','','','')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))
        
class SourceTest(unittest.TestCase):
    
    def setUp(self):
        
        self.new_source = Source('','','','','','')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source)) 
        
if __name__ == '__main__':
    unittest.main()
