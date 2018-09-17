from firstfood import app 
from firstfood import orders
import unittest


class apiEndpoints(unittest.TestCase):
    
    
    # Ensure that flask is working
    def test_welcome(self):
        tester = app.test_client(self)
        response = tester.get('/v1', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to Farst Foods Farst!.Please Sign up:', response.data)
        
    # Ensure All orders orders are returned
    def test_returnAll(self):
        tester = app.test_client(self)
        response = tester.get(
            '/api/v1/all_orders', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        

    # Ensure that new order is created
    def test_addOrder(self):
        tester = app.test_client(self)
        self.orders = [{'name':'coffee'}, {'name':'Beaf'},{'name' : 'Milk'}]
        self.order= {'name':'Bread'}
        self.new_orders=orders.append(self.order)
        response = tester.post(
            '/api/v1/all_orders', data = self.new_orders)
        self.assertTrue(response.status_code, 201 )

    
    # Ensure status of an order is Updated
    def test_editOrder(self):
        tester = app.test_client(self)
        self.orders = [{'name':'coffee'}, {'name':'Beaf'},{'name' : 'Milk'}]
        self.order= {'name':'Tea'}
        self.new_orders= [order for order in orders if order['name']== ['coffee']]
        self.orders[0]['name'] = self.order
        response = tester.put(
            '/api/v1/all_orders' , data = self.new_orders)
        self.assertTrue(response.status_code, 201)

    # Ensure  an order is deleted
    def test_deleteOrder(self):
        tester = app.test_client(self)
        self.orders = [{'name':'coffee'}, {'name':'Beaf'},{'name' : 'Milk'}]
        self.new_orders=[order for order in orders if order['name']== ['coffee']]
        self.orders.remove(self.orders[0])
        return self.new_orders
        response = tester.delete(
            '/api/v1/all_orders' , data = self.new_orders)
        self.assertTrue(response.status_code, 200)
        self.assertEqual(self.new_orders,[{'name':'Beaf'},{'name' : 'Milk'}])
    
    def test_login(self):
        tester = app.test_client(self)
        response = tester.post(
            '/v1/login',
            data=dict(username="domnic", password="domnic"),
            follow_redirects=True 
        )
        self.assertIn(b'Please Make your order', response.data)



if __name__ == '__main__':
    unittest.main()

