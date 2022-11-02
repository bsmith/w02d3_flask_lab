from app import app
from models import order_list
from flask import render_template
from datetime import datetime

@app.route('/orders')
def orders():
    today = datetime.now().strftime("%A %d %b %Y")
    return render_template('orders.html.j2', orders=order_list.orders, today=today)

@app.route('/orders/<int:index>')
def orders_view_one(index):
    return render_template('order.html', order=order_list.orders[index], index=index)
