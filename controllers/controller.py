from app import app
from models import order_list
from flask import render_template

@app.route('/orders')
def orders():
    return render_template('orders.html.j2', orders=order_list.orders)

@app.route('/orders/<index>')
def orders_view_one(index):
    return render_template('order.html', order=order_list.orders[int(index)])
