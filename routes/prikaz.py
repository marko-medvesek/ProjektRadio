from flask import Blueprint,render_template, jsonify, request
from urllib.parse import urlparse, parse_qs
import requests
import json


import routes.seznam as seznam


bp = Blueprint("prikaz", __name__)

@bp.route('/prikaz')
def get_incomes():
    #print(json.dumps(seznam.getSeznam(), indent=4, sort_keys=True))
    return render_template('prikaz.html', data=seznam.getSeznam())

