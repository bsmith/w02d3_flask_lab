from flask import Flask, render_template
from controllers.orders import orders

app = Flask(__name__)
app.register_blueprint(orders)

if __name__ == "__main__":
    app.run(debug=True)
