from flask import Flask

from routes import pages
from routes import seznam
from routes import prikaz

def create_app():
    app = Flask(__name__, template_folder='static/pages')

    app.register_blueprint(pages.bp)
    app.register_blueprint(seznam.bp)
    app.register_blueprint(prikaz.bp)
    return app