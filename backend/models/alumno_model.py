import json
from factory import db

alumnos_planificaciones = db.Table("alumnos_planificaciones",
                                   db.Column("id_alumno_planificacion", db.Integer, primary_key=True),
                                   db.Column("id_alumno", db.Integer, db.ForeignKey("alumno.id_alumno")),
                                   db.Column("id_planificacion", db.Integer, db.ForeignKey("planificacion.id_planificacion")))


class Alumno(db.Model):

    __tablename__ = "alumno"

    id_alumno = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'))

    estado = db.Column(db.String(45), nullable=False)
    planilla_medica = db.Column(db.Boolean, nullable=False)

    usuario = db.relationship('Usuario', back_populates='alumno', uselist=False, cascade="all, delete-orphan", single_parent=True, lazy='joined')
    planificaciones = db.relationship('Planificacion', secondary=alumnos_planificaciones, backref="alumnos")

    def __init__(self, estado=None, planilla_medica=None):
        self.estado = estado
        self.planilla_medica = planilla_medica

    def __repr__(self):
        return f'<alumno: {self.id_alumno} >'

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
        return Alumno(**data_dict)

    def to_json_complete(self):
        """Return a complete JSON representation of the Alumno object."""
        alumno_json = {
            'id_alumno': self.id_alumno,
            'id_usuario': self.id_usuario,
            'estado': self.estado,
            'planilla_medica': self.planilla_medica,
            "usuario": self.usuario.to_json(),
            "planificaciones": [planificacion.to_json() for planificacion in self.planificaciones]
        }
        return alumno_json
