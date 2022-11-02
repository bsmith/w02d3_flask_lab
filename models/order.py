from datetime import date, time, datetime, timedelta;

class Order:
    def __init__(self, customer_name, order_date, quantity, food_topping):
        self.customer_name = customer_name
        self.order_date = order_date
        self.quantity = quantity
        self.food_topping = food_topping

    def format_order_date_as_string(self):
        today_start = datetime.combine(date.today(), time(0, 0, 0))
        if self.order_date - today_start < timedelta(days=1):
            return self.order_date.strftime("today %H:%M:%S")
        return self.order_date.strftime("%A %d %b %y %H:%M:%S")