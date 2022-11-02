from flask import Flask, render_template
from controllers.orders import orders

# App Factory Pattern: https://flask.palletsprojects.com/en/2.2.x/patterns/appfactories/
def create_app():
    app = Flask(__name__)
    app.register_blueprint(orders)
    return app

if __name__ == "__main__":
    app = create_app()
    # app.run(debug=True)
    app.run()
