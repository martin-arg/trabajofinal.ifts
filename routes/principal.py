from flask import Blueprint, render_template
from flask_login import login_required, current_user

principal = Blueprint('principal', __name__)


@principal.route('/')
def index():
    return render_template('index.html')


@principal.route('/actividades')
def actividades():
    return render_template('actividades.html')


@principal.route('/contacto')
def contactos():
    return render_template('contacto.html')


@principal.route('/instalaciones')
def instalaciones():
    return render_template('instalaciones.html')


@principal.route('/profile')
@login_required
def profile():
    return render_template('views/profile.html', name=current_user.nombre)

@principal.route('/crearsocios')
@login_required
def enviar_crearsocios():
    return render_template('views/createSocios.html')
