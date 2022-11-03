from flask import Flask, render_template
from controllers.orders import orders

# App Factory Pattern: https://flask.palletsprojects.com/en/2.2.x/patterns/appfactories/
def create_app():
    app = Flask(__name__)
    app.register_blueprint(orders)

    @app.errorhandler(404)
    def page_not_found(e):
        return """<img src="https://http.cat/404.jpg">"""

    return app

if __name__ == "__main__":
    app = create_app()
    # app.run(debug=True)
    app.run()
