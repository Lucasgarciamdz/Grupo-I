import json
from factory import db


class Planificacion(db.Model):

    __tablename__ = "planificacion"

    id_planificacion = db.Column(db.Integer, primary_key=True)
    id_clase = db.Column(db.Integer, db.ForeignKey('clase.id_clase'))

    nombre = db.Column(db.String(45))
    horas_semanales = db.Column(db.Integer)
    objetivo = db.Column(db.String(45))

    clase = db.relationship('Clase',
                            back_populates='planificacion',
                            single_parent=True,
                            uselist=False,
                            cascade="all, delete-orphan",
                            passive_deletes=True,
                            lazy='joined',
                            innerjoin=True,
                            post_update=True,
                            foreign_keys=[id_clase])

    def __init__(self, nombre=None, horas_semanales=None, objetivo=None):
        self.nombre = nombre
        self.horas_semanales = horas_semanales
        self.objetivo = objetivo

    def __repr__(self):
        return f'<planificacion: {self.id_planificacion} >'

    def to_json(self):
        db.session.refresh(self)
        data = self.__dict__.copy()
        del data['_sa_instance_state']
        del data['contrasena']
        return data

    @staticmethod
    def from_json(json_data):
        if isinstance(json_data, str):
            data_dict = json.loads(json_data)
        elif isinstance(json_data, dict):
            data_dict = json_data
        else:
            raise ValueError("Invalid JSON data")
        return Planificacion(**data_dict)

    def to_json_complete(self):
        planificacion_json = {
            'id_planificacion': self.id_planificacion,
            'id_clase': self.id_clase,
            'horas_semanales': self.horas_semanales,
            'objetivo': self.objetivo,
            'alumnos': [alumno.to_json() for alumno in self.alumnos],
            'clase': self.clase.to_json()
        }
        return planificacion_json
