import unittest


# local imports
from firstfood import orders
from firstfood import app 


class TestapiEndpoints(unittest.TestCase):

    # ensuring jsonify returns the right output
    def test_output(self):
        self.client = app.test_client(self)
        self.data={'message' : 'Itworks!'}
        self.output = self.client.get(
            '/api/v1/order', data=self.data)
        self.assertEqual(self.output.status_code, 200)
        

    # Ensure All orders orders are returned
    def test_returnAll(self):
        self.client = app.test_client(self)
        self.output = self.client.get(
            '/api/v1/all_orders', content_type='html/text')
        self.assertEqual(self.output.status_code, 200)

    # Ensure one order is returned
    def test_returnOne(self):
        self.client = app.test_client(self)
        self.order= "Beef"
        self.ords=[order for order in orders if order['name']== self.order]
        return self.order       
        self.output=self.client.get(
            '/api/v1/all_orders/<string:name>', data=self.ords)
        self.assertEqual(self.output.status_code, 200)

        

    # Ensure that new order is created
    def test_addOrder(self):
        self.client = app.test_client(self)
        self.orders = [{'name':'coffee'}, {'name':'Beaf'},{'name' : 'Milk'}]
        self.order= {'name':'Bread'}
        self.new_orders=orders.append(self.order)
        self.output = self.client.post(
            '/api/v1/all_orders', data = self.new_orders)
        self.assertTrue(self.output.status_code, 201 )

    
    # Ensure status of an order is Updated
    def test_editOrder(self):
        self.client = app.test_client(self)
        self.orders = [{'name':'coffee'}, {'name':'Beaf'},{'name' : 'Milk'}]
        self.order= {'name':'Tea'}
        self.new_orders= [order for order in orders if order['name']== ['coffee']]
        self.orders[0]['name'] = self.order
        self.output = self.client.put(
            '/api/v1/all_orders' , data = self.new_orders)
        self.assertTrue(self.output.status_code, 201)

        
    # Ensure  an order is deleted
    def test_deleteOrder(self):
        self.client = app.test_client(self)
        self.orders = [{'name':'coffee'}, {'name':'Beaf'},{'name' : 'Milk'}]
        self.new_orders=[order for order in orders if order['name']== ['coffee']]
        self.orders.remove(self.orders[0])
        return self.new_orders
        self.output = self.client.delete(
            '/api/v1/all_orders' , data = self.new_orders)
        self.assertTrue(self.output.status_code, 200)
        self.assertEqual(self.new_orders,[{'name':'Beaf'},{'name' : 'Milk'}])
    
    
   
   
if __name__ == '__main__':
    unittest.main()

