from models.order import Order
import datetime

order1 = Order("Mar",
    datetime.datetime(2022, 11, 2, 12, 5, 0),
    2, "pepperoni")
order2 = Order("Colette", 
    datetime.datetime(2022, 11, 2, 12, 12, 30),
     5, "hawaiian")
orders = [order1, order2]


for x in [1, 2, 3]:
    orders.append(
        Order("James", datetime.datetime(2022, 11, 2, 12, 12, 30),
            10, "four cheese"))
    