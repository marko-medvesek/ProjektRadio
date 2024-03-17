from flask import Flask

from routes import pages
from routes import seznam
from routes import static

def create_app():
    app = Flask(__name__, template_folder='static/pages')
    app.config['TEMPLATES_AUTO_RELOAD'] = True

    app.register_blueprint(pages.bp)
    app.register_blueprint(seznam.bp)
    app.register_blueprint(static.bp)
    return app