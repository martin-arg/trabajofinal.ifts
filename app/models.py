from app import db

class Reserva(db.Model):
    __tablename__ = 'reservas'
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, nullable=False)
    fecha = db.Column(db.String(10), nullable=False)
    habitacion = db.Column(db.Integer, nullable=False)
    duracion = db.Column(db.Integer, nullable=False)