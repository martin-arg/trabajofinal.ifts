from flask_login import UserMixin
from extensiones import db


class Usuarios(UserMixin, db.Model):  # ✅ correcto
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(100))
    clave = db.Column(db.String(100))
    rol = db.Column(db.String(100))
    nombre = db.Column(db.String(100))
    apellido = db.Column(db.String(100))
