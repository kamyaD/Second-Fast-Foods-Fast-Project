from firstfood import app 
from firstfood import orders
import unittest

class WelcomeTestCase(unittest.TestCase):
    
    # Ensure that flask is working
    def test_welcome(self):
        tester = app.test_client(self)
        response = tester.get('/v1', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensure Welcome page has correct content    
    def test_content(self):
        tester = app.test_client(self)
        response = tester.get('/v1', content_type='html/text')
        self.assertTrue(b'Fast Foods Fast' in response.data)
    
    # Ensure All orders orders are returned
    def test_returnAll(self):
        tester = app.test_client(self)
        response = tester.get(
            '/api/v1/all_orders', content_type='html/text')
        self.assertTrue(b'coffee' in response.data)


if __name__ == '__main__':
    unittest.main()
