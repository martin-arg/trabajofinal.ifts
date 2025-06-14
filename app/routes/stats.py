from flask import Blueprint, render_template

bp = Blueprint('stats', __name__)

@bp.route('/estadisticas')
def estadisticas():
    return render_template('estadisticas.html')
