import unittest
from firstfood import *
from flask import jsonify

class test_odres_returnAll(unittest.TestCase):
    def test_return_all_orders(self):
        response = self.getOrders()
        result = jsonify({'message' : 'Itworks!'})
        self.assertEqual(response, result)

if __name__ == '__main__':
    unittest.main()