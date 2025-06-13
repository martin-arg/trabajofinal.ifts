from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required, login_manager
import models.usuarios

auth = Blueprint('auth', __name__)


@auth.route("/sign-up", methods=['GET', 'POST'])
def login():
    usuario = request.form.get('usuario')
    # clave = request.form.get('password')
    user = models.usuarios.Usuarios.query.filter_by(usuario=usuario).first()
    # passwd = models.usuarios.Usuarios.query.filter_by(clave=clave).first()
    if user:
        login_user(user, remember=True)

        return redirect(url_for('principal.profile'))
        return render_template('views/profile.html')

    return redirect(url_for('auth.sign-up'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return render_template('index.html')

