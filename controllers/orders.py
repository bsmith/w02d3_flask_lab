from models import order_list
from flask import Blueprint, render_template
from datetime import datetime

# Blueprints! https://flask.palletsprojects.com/en/2.2.x/blueprints/

orders = Blueprint("orders", __name__)

@orders.route("/")
def index_page():
    return render_template("index.html.j2")

@orders.route('/orders')
def orders_list():
    today = datetime.now().strftime("%A %d %b %Y")
    return render_template('orders.html.j2', orders=order_list.orders, today=today)

@orders.route('/orders/<int:index>')
def orders_view_one(index):
    return render_template('order.html.j2', order=order_list.orders[index], index=index)
