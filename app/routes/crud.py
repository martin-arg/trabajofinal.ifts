from flask import Blueprint, render_template, request, redirect, url_for
from app.models import db, Reserva

bp = Blueprint('crud', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/reservas', methods=['GET', 'POST'])
def reservas():
    if request.method == 'POST':
        # Alta nueva reserva
        cliente_id = request.form['cliente_id']
        fecha = request.form['fecha']
        habitacion = request.form['habitacion']
        duracion = request.form['duracion']

        nueva = Reserva(
            cliente_id=cliente_id,
            fecha=fecha,
            habitacion=habitacion,
            duracion=duracion
        )
        db.session.add(nueva)
        db.session.commit()
        return redirect(url_for('crud.reservas'))

    # Búsqueda por cliente_id si se envió
    filtro_id = request.args.get('cliente_id')
    if filtro_id:
        reservas = Reserva.query.filter_by(cliente_id=filtro_id).all()
    else:
        reservas = Reserva.query.all()

    return render_template('reservas.html', reservas=reservas)


@bp.route('/reservas/editar/<int:id>', methods=['GET', 'POST'])
def editar_reserva(id):
    reserva = Reserva.query.get_or_404(id)
    if request.method == 'POST':
        reserva.cliente_id = request.form['cliente_id']
        reserva.fecha = request.form['fecha']
        reserva.habitacion = request.form['habitacion']
        reserva.duracion = request.form['duracion']
        db.session.commit()
        return redirect(url_for('crud.reservas'))

    return render_template('editar_reserva.html', reserva=reserva)


@bp.route('/reservas/borrar/<int:id>', methods=['POST'])
def borrar_reserva(id):
    reserva = Reserva.query.get_or_404(id)
    db.session.delete(reserva)
    db.session.commit()
    return redirect(url_for('crud.reservas'))
