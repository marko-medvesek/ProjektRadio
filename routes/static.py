from flask import send_from_directory, Blueprint

bp = Blueprint("static", __name__)


@bp.route('/static/<path:path>')
def send_report(path):
    return send_from_directory('reports', path)