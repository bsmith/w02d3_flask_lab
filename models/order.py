class Order:
    def __init__(self, customer_name, order_date, quantity, food_topping):
        self.customer_name = customer_name
        self.order_date = order_date
        self.quantity = quantity
        self.food_topping = food_topping

    def format_order_date_as_string(self):
        return self.order_date.strftime("%A %d %b %y %H:%M:%S")