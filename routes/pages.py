from flask import Blueprint,render_template

bp = Blueprint("pages", __name__)

@bp.route("/")
def home():
    return render_template('index.html')

@bp.route("/about")
def about():
    return "Hello, About!"
