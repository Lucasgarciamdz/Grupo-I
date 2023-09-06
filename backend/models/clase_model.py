import json
from factory import db


class Clase(db.Model):

    __tablename__ = "clase"

    id_clase = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(45), nullable=False)

    planificacion = db.relationship('Planificacion', back_populates='clase', cascade="all, delete-orphan", single_parent=True)

    def __init__(self, nombre=None):
        self.nombre = nombre

    def __repr__(self):
        return f'<clase: {self.id_clase} >'

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
        return Clase(**data_dict)

    def to_json_complete(self):
        clase_json = {
            'id': self.id_clase,
            'nombre': self.nombre,
            'planificacion': self.planificacion.to_json(),
            'profesores': [profesor.to_json() for profesor in self.profesores]
        }
        return clase_json
