from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
import models.actividades
import models.socios
from extensiones import db, ma


class Clases(db.Model):
    actividadID = db.Column(db.Integer, ForeignKey("actividades.actividadID"), primary_key=True)
    socioID = db.Column(db.Integer, ForeignKey("socios.socioID"), primary_key=True)
    # socios = relationship('')

    def __init__(self, actividadID, socioID):
        self.actividadID = actividadID
        self.socioID = socioID
