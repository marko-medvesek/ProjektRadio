from flask import Blueprint, render_template, Response

bp = Blueprint("pages", __name__)

import routes.seznam as seznam


@bp.route("/")
def home():
    return render_template("lestvica.html", data=seznam.getSeznam())


@bp.route("/prikaz")
def get_incomes():
    # print(json.dumps(seznam.getSeznam(), indent=4, sort_keys=True))
    return render_template("prikaz.html", data=seznam.getSeznam())


@bp.route("/status")
def success():
    return Response("Success", status=200, mimetype="application/json")


@bp.route("/404")
def about():
    return render_template("err/404.html"), 404


@bp.route("/lestvica")
def lestvica():
    return render_template("lestvica.html", data=seznam.getSeznam())
