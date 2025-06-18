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

@bp.route('/estadisticas/linea_mensual')
def grafico_linea_mensual():
    reservas = Reserva.query.all()
    df = pd.DataFrame([{"fecha": r.fecha} for r in reservas])
    df["mes"] = pd.to_datetime(df["fecha"]).dt.to_period("M").astype(str)

    conteo = df["mes"].value_counts().sort_index()

    fig, ax = plt.subplots()
    conteo.plot(kind='line', marker='o', ax=ax)
    ax.set_title("Reservas por Mes")
    ax.set_xlabel("Mes")
    ax.set_ylabel("Cantidad de reservas")
    plt.xticks(rotation=45)
    plt.tight_layout()

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    return send_file(img, mimetype='image/png')


@bp.route('/estadisticas/boxplot_duracion')
def boxplot_duracion_por_planta():
    reservas = Reserva.query.all()
    df = pd.DataFrame([{
        "planta": str(r.habitacion)[0],
        "duracion": r.duracion
    } for r in reservas])

    fig, ax = plt.subplots()
    import seaborn as sns
    sns.boxplot(x="planta", y="duracion", data=df, ax=ax)
    ax.set_title("Duración de reservas por planta")
    ax.set_xlabel("Planta")
    ax.set_ylabel("Duración (días)")
    plt.tight_layout()

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    return send_file(img, mimetype='image/png')


@bp.route('/estadisticas/heatmap')
def heatmap_planta_vs_duracion():
    reservas = Reserva.query.all()
    df = pd.DataFrame([{
        "planta": str(r.habitacion)[0],
        "duracion": r.duracion
    } for r in reservas])

    tabla = df.pivot_table(index="planta", columns="duracion", aggfunc="size", fill_value=0)

    fig, ax = plt.subplots(figsize=(10, 5))
    import seaborn as sns
    sns.heatmap(tabla, cmap="YlGnBu", annot=True, fmt="d", ax=ax)
    ax.set_title("Heatmap: Frecuencia por planta y duración")
    plt.tight_layout()

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    return send_file(img, mimetype='image/png')

@bp.route('/estadisticas/grafico_completo')
def grafico_completo():
    reservas = Reserva.query.all()
    df = pd.DataFrame([{
        "habitacion": r.habitacion,
        "fecha": r.fecha,
        "duracion": r.duracion
    } for r in reservas])

    df["planta"] = df["habitacion"].astype(str).str[0]
    df["mes"] = pd.to_datetime(df["fecha"]).dt.to_period("M").astype(str)

    # Datos para cada gráfico
    por_habitacion = df["habitacion"].value_counts().sort_index()
    por_planta = df["planta"].value_counts().sort_index()
    por_mes = df["mes"].value_counts().sort_index()
    duraciones = df["duracion"]

    # Crear figura con 2x2 subplots
    fig, axs = plt.subplots(2, 2, figsize=(12, 8))

    # Gráfico de barras
    por_habitacion.plot(kind="bar", ax=axs[0, 0], color="skyblue")
    axs[0, 0].set_title("Reservas por habitación")
    axs[0, 0].set_xlabel("Habitación")
    axs[0, 0].set_ylabel("Cantidad")

    # Gráfico de torta
    axs[0, 1].pie(por_planta, labels=por_planta.index, autopct="%1.1f%%", startangle=90)
    axs[0, 1].set_title("Distribución por planta")

    # Gráfico de línea
    por_mes.plot(kind="line", marker="o", ax=axs[1, 0])
    axs[1, 0].set_title("Reservas por mes")
    axs[1, 0].set_xlabel("Mes")
    axs[1, 0].set_ylabel("Cantidad")
    axs[1, 0].tick_params(axis='x', rotation=45)

    # Histograma
    duraciones.plot(kind="hist", bins=10, ax=axs[1, 1])
    axs[1, 1].set_title("Duración de reservas")
    axs[1, 1].set_xlabel("Días")
    axs[1, 1].set_ylabel("Frecuencia")

    plt.tight_layout()
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    return send_file(img, mimetype='image/png')