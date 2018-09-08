from firstfood import app 
import unittest

class WelcomeTestCase(unittest.TestCase):
    
    #Ensure that flask is working
    def test_welcome(self):
        tester = app.test_client(self)
        response = tester.get('/v1', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        
    
    


if __name__ == '__main__':
    unittest.main()
