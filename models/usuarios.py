import app
from flask_login import UserMixin


class Usuarios(UserMixin, app.db.Model):
    id = app.db.Column(app.db.Integer, primary_key=True)
    usuario = app.db.Column(app.db.String(100))
    clave = app.db.Column(app.db.String(100))
    rol = app.db.Column(app.db.String(100))
    nombre = app.db.Column(app.db.String(100))
    apellido = app.db.Column(app.db.String(100))
