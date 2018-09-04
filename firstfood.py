from flask import Flask, render_template, jsonify, request #import objects from the Flask model

app = Flask(__name__, template_folder='v1') #define app and telling flask that template folder is named v1
orders = [{'name':'coffee'}, {'name':'Beaf'}]

@app.route('/v1')
def welcome():
    return render_template("welcome.html")

@app.route('/v1/order', methods=['GET'])
def getOrders():
    return jsonify({'message' : 'Itworks!'})

@app.route('/v1/all_orders', methods=['GET']) # GET API that gets all orders
def returnAll():
    return jsonify({'orders': orders})

@app.route('/v1/all_orders/<string:name>', methods=['GET']) # fetch Specific order
def returnOne(name):
    ords=[order for order in orders if order['name']== name]
    return jsonify({'order' : ords[0]})





if __name__ == '__main__':
    app.run(debug=True)