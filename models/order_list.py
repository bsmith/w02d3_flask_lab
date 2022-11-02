from models.order import Order
from datetime import datetime, date, time

orders = []

orders.append(Order("Mar",
    datetime.combine(date.today(), time(12, 5, 0)),
    2, "pepperoni"))
orders.append(Order("Colette", 
    datetime.combine(date.today(), time(12, 12, 30)),
     5, "hawaiian"))
orders.append(Order("Keith", 
    datetime.combine(date.today(), time(12, 12, 30)),
     1, "margherita"))

for x in [1, 2, 3]:
    orders.append(
        Order("James", datetime(2022, 11, 2, 12, 12, 30),
            10, "four cheese"))
    