from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
import models.actividades
import models.socios
import app


class Clases(app.db.Model):
    actividadID = app.db.Column(app.db.Integer, ForeignKey("actividades.actividadID"), primary_key=True)
    socioID = app.db.Column(app.db.Integer, ForeignKey("socios.socioID"), primary_key=True)
    # socios = relationship('')

    def __init__(self, actividadID, socioID):
        self.actividadID = actividadID
        self.socioID = socioID
