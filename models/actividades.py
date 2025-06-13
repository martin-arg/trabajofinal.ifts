from sqlalchemy import ForeignKey
from extensiones import db, ma



class Actividades(db.Model):
    actividadID = db.Column(db.Integer, primary_key=True)
    actividad = db.Column(db.String(100))
    responsableID = db.Column(db.Integer, ForeignKey('usuarios.id'))
    dias = db.Column(db.String(100))
    horario = db.Column(db.String(100))
    asistentesMax = db.Column(db.Integer)
    responsable = db.relationship("Usuarios", primaryjoin="and_(Actividades.responsableID==Usuarios.id) ")
    clases = db.relationship('Clases', passive_deletes=True)
