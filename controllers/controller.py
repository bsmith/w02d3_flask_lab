from app import app
from models import order_list
from flask import render_template

@app.route('/orders')
def orders():
    return render_template('orders.html.j2', orders=order_list.orders)