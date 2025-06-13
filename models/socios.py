from sqlalchemy.orm import relationship
import models.clases
from extensiones import db, ma


class Socios(db.Model):
    socioID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    dni = db.Column(db.Integer)
    email = db.Column(db.String(100))
    clases = db.relationship('Clases', cascade='save-update, merge, delete')

    def __init__(self, name, dni, email):
        self.name = name
        self.dni = dni
        self.email = email

# passive_deletes=True,
