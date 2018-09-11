from firstfood import app 
from firstfood import orders
import unittest
import json

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

    def test_addOrder(self):
        tester = app.test_client(self)
        self.orders = [{'name':'coffee'}, {'name':'Beaf'},{'name' : 'Milk'}]
        self.order= {'name':'Bread'}
        self.new_orders=orders.append(self.order)
        response = tester.post(
            '/api/v1/all_orders', data= self.new_orders)
        self.assertTrue(response.status_code, 201 )

        
if __name__ == '__main__':
    unittest.main()

