from flask import Blueprint, render_template, send_file
import io
import matplotlib.pyplot as plt
import pandas as pd
from app.models import db, Reserva

bp = Blueprint('stats', __name__)


@bp.route('/estadisticas')
def estadisticas():
    return render_template('estadisticas.html')


@bp.route('/estadisticas/grafico_barras')
def grafico_barras():
    reservas = Reserva.query.all()
    df = pd.DataFrame([{
        "habitacion": r.habitacion
    } for r in reservas])

    conteo = df["habitacion"].value_counts().sort_index()

    fig, ax = plt.subplots()
    conteo.plot(kind='bar', ax=ax)
    ax.set_title("Habitaciones más reservadas")
    ax.set_xlabel("Habitación")
    ax.set_ylabel("Cantidad de reservas")
    plt.tight_layout()

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    return send_file(img, mimetype='image/png')


@bp.route('/estadisticas/histograma')
def histograma_duracion():
    reservas = Reserva.query.all()
    df = pd.DataFrame([{
        "duracion": r.duracion
    } for r in reservas])

    fig, ax = plt.subplots()
    df["duracion"].plot(kind='hist', bins=10, ax=ax)
    ax.set_title("Histograma de duración de reservas")
    ax.set_xlabel("Duración (días)")
    ax.set_ylabel("Frecuencia")
    plt.tight_layout()

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    return send_file(img, mimetype='image/png')


@bp.route('/estadisticas/torta_plantas')
def torta_por_planta():
    reservas = Reserva.query.all()
    df = pd.DataFrame([{
        "habitacion": r.habitacion
    } for r in reservas])

    # Planta = primer dígito de la habitación
    df["planta"] = df["habitacion"].astype(str).str[0]
    conteo = df["planta"].value_counts().sort_index()

    fig, ax = plt.subplots()
    conteo.plot(kind='pie', autopct='%1.1f%%', ax=ax)
    ax.set_ylabel("")
    ax.set_title("Distribución de reservas por planta")
    plt.tight_layout()

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    return send_file(img, mimetype='image/png')
