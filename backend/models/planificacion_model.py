from app import db
from .alumno_model import alumnos_planificaciones


class Planificacion(db.Model):

    __tablename__ = "planificacion"

    id_planificacion = db.Column(db.Integer, primary_key=True)
    id_clase = db.Column(db.Integer, db.ForeignKey('clase.id_clase'))

    nombre = db.Column(db.String(45))
    horas_semanales = db.Column(db.Integer)
    objetivo = db.Column(db.String(45))

    alumnos = db.relationship('Alumno', secondary=alumnos_planificaciones, backref=db.backref('planificaciones_a', lazy='dynamic'))
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

    def __repr__(self):
        return '<planificacion: %r >' % (self.id_planificacion)

    def to_json(self):
        planificacion_json = {
            'id_planificacion': self.id_planificacion,
            'id_clase': self.id_clase,
            'horas_semanales': self.horas_semanales,
            'objetivo': self.objetivo,
        }
        return planificacion_json

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

    @staticmethod
    def from_json(planificacion_json):
        id_planificacion = planificacion_json.get('id_planificacion')
        id_clase = planificacion_json.get('id_clase')
        horas_semanales = planificacion_json.get('horas_semanales')
        objetivo = planificacion_json.get('objetivo')
        return Planificacion(id_planificacion=id_planificacion,
                             id_clase=id_clase,
                             horas_semanales=horas_semanales,
                             objetivo=objetivo,
                             )
