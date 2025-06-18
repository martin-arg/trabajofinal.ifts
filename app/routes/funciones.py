from flask import Blueprint, redirect, url_for, render_template, request, send_file, current_app
from app.models import db, Reserva
import random
import datetime
import json
import os

bp = Blueprint('funciones', __name__)

##### Llama a las paginas de funciones


@bp.route('/funciones')
def index_funciones():
    return render_template('funciones.html')

@bp.route('/funciones/cargar_datos')
def cargar_datos_de_prueba():
    # (opcional) Borra datos anteriores
    db.session.query(Reserva).delete()

    for _ in range(100):
        reserva = Reserva(
            cliente_id=random.randint(100000, 999999),
            fecha=(datetime.date.today() - datetime.timedelta(days=random.randint(0, 365))).isoformat(),
            habitacion=random.randint(100, 499),
            duracion=random.randint(1, 10)
        )
        db.session.add(reserva)

    db.session.commit()
    return redirect(url_for('crud.reservas'))

@bp.route('/funciones/exportar_cliente', methods=['GET', 'POST'])
def exportar_cliente():
    if request.method == 'POST':
        cliente_id = request.form.get('cliente_id')

        if not cliente_id:
            return "Debe ingresar un ID de cliente", 400

        reserva = Reserva.query.filter_by(cliente_id=cliente_id).first()
        if not reserva:
            return f"No se encontró reserva para cliente {cliente_id}", 404

        datos = {
            "cliente_id": reserva.cliente_id,
            "fecha": reserva.fecha,
            "habitacion": reserva.habitacion,
            "duracion": reserva.duracion
        }

        file_path = os.path.join(current_app.instance_path, f"cliente_{cliente_id}.json")
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(datos, f, indent=4)

        return send_file(file_path, as_attachment=True)

    return render_template('exportar_cliente.html')