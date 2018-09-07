from flask import Flask, render_template, jsonify, request 
import unittest
from  firstfood import returnAll

class test_odres_returnAll(unittest.TestCase):
    def test_return_all_orders(self):
        all=self.returnAll().get(
            '/api/v1/all_orders',
            orders = [{'name':'coffee'}, {'name':'Beaf'},{'name' : 'Milk'}]) 
        self.assertEqual(all.status_code, 200)
    


if __name__ == "__main__":
    unittest.main()