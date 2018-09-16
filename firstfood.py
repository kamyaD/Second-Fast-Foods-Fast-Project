#import objects from the Flask model
from flask import Flask, render_template, jsonify, request,session,flash,redirect,url_for 

app = Flask(__name__, template_folder='v1') #define app and telling flask that template folder is named v1
orders = [{'name':'coffee'}, {'name':'Beaf'},{'name' : 'Milk'}] # Making a Dictionary of orders that is to be used to test the code
app.secret_key= "I love kenya"

@app.route('/v1')
def welcome():
    return render_template("welcome.html") 

@app.route('/v1/histry')
def histry():
    return render_template("histry.html")


@app.route('/v1/order')
def order():
    return render_template("order.html")

@app.route('/v1/add_order')
def add_order():
    return render_template("add_order.html")

@app.route('/api/v1/order', methods=['GET']) #Testing the jsonify out put on a browser
def getOrders():
    return jsonify({'message' : 'Itworks!'})

@app.route('/api/v1/all_orders', methods=['GET']) # GET API that gets all orders
def returnAll():
    return jsonify({'orders': orders})

@app.route('/api/v1/all_orders/<string:name>', methods=['GET']) # fetch Specific order
def returnOne(name):
    ords=[order for order in orders if order['name']== name]
    return jsonify({'order' : ords[0]})

@app.route('/api/v1/all_orders', methods=['POST']) # Places a new Order
def addOrder():
    order = request.get_json('name')
    orders.append(order)
    return jsonify({'orders' : orders})

@app.route('/api/v1/all_orders/<string:name>', methods=['PUT']) # Update the status of an order
def editOrder(name):
    ords=[order for order in orders if order['name']== name]
    ords[0]['name'] = request.get_json(['name'])
    return jsonify({'order' : ords[0]})

@app.route('/api/v1/all_orders/<string:name>', methods=['Delete']) # Delete an order
def deleteOrder(name):
    delOrder=[order for order in orders if order['name']== name]
    orders.remove(delOrder[0])
    return jsonify({'orders': orders})

@app.route('/v1/login', methods=['GET','POST']) # Login APIs
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'domnic' or request.form['password'] != 'domnic':
            error='Invalid credentials. Please try again.'
        else:
            session['logged_in'] = True
            #flash('You are now logged in!')
            return redirect(url_for('order'))
    return render_template('login.html', error=error)

@app.route('/v1/logout')
def logout():
    session.pop('logged_in',None)
    flash('You are now  loged out!')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=False)
