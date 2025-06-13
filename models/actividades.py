from sqlalchemy import ForeignKey

import app


class Actividades(app.db.Model):
    actividadID = app.db.Column(app.db.Integer, primary_key=True)
    actividad = app.db.Column(app.db.String(100))
    responsableID = app.db.Column(app.db.Integer, ForeignKey('usuarios.id'))
    dias = app.db.Column(app.db.String(100))
    horario = app.db.Column(app.db.String(100))
    asistentesMax = app.db.Column(app.db.Integer)
    responsable = app.db.relationship("Usuarios", primaryjoin="and_(Actividades.responsableID==Usuarios.id) ")
    clases = app.db.relationship('Clases', passive_deletes=True)
