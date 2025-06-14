from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Reserva(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, nullable=False)
    fecha = db.Column(db.String(10), nullable=False)
    habitacion = db.Column(db.Integer, nullable=False)
    duracion = db.Column(db.Integer, nullable=False)
