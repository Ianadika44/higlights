import unittest
from models import article
Article = article.Article


class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''

        self.new_article = Article('','','','','','','','')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))
        
class SourceTest(unittest.TestCase):
    """
    Test Class to test behaviour of source class
    """
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Source('','','','','','')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source)) 
        
if __name__ == '__main__':
    unittest.main()
