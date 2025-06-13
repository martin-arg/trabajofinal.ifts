from flask import Blueprint, render_template, redirect, url_for, request, flash

from models.actividades import Actividades
from models.socios import Socios
import app
from models.usuarios import Usuarios

profile = Blueprint('profile', __name__)


@profile.route('/socioslistar')
def socios_listar():
    listaSocios = Socios.query.all()

    return render_template('views/socios.html', listaSocios=listaSocios)


@profile.route('/socioscrear', methods=['POST'])
def socios_crear():
    nombre = request.form.get('nombre')
    dni = request.form.get('dni')
    email = request.form.get('email')
    new_socio = Socios(nombre, dni, email)
    app.db.session.add(new_socio)
    app.db.session.commit()
    return render_template('views/createSocios.html')


@profile.route("/modificarSocios/<string:id>", methods=['POST', 'GET'])
def socios_modificar(id):
    socio = Socios.query.get(id)
    if request.method == "POST":
        socio.name = request.form["name"]
        socio.email = request.form["email"]
        socio.dni = request.form["dni"]
        app.db.session.commit()
        flash('Contact updated successfully!')
        return redirect(url_for('profile.socios_listar'))
    return render_template('views/modificarSocios.html', socio=socio)


@profile.route('/sociosborrar/<id>')
def socios_borrar(id):
    socio = Socios.query.get(id)
    app.db.session.delete(socio)
    app.db.session.commit()
    return redirect(url_for('profile.socios_listar'))


@profile.route('/listaractividades')
def actividades_listar():
    listaActividades = Actividades.query.all()

    return render_template('views/listarActividades.html', listaActividades=listaActividades)


@profile.route('/listarclases')
def clases_listar():
    return render_template('views/listarSocios.html')


@profile.route('/listarusuarios')
def usuarios_listar():
    listarUsuarios = Usuarios.query.all()
    return render_template('views/listarUsuarios.html', listarUsuarios=listarUsuarios)
