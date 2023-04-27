from .. import db


class Planificacion(db.Model):

    __tablename__ = "planificacion"

    id_planificacion = db.Column(db.Integer, primary_key=True)
    id_clase = db.Column(db.Integer, db.ForeignKey('clase.id_clase'))
    
    horas_semanales = db.Column(db.Integer)
    objetivo = db.Column(db.String(45))

    planificacion_alumno = db.relationship('AlumnoPlanificacion', back_populates='planificacion', cascade="all, delete-orphan")
    clase = db.relationship('Clase', back_populates='planificacion', cascade="all, delete-orphan")
    clase_profesor = db.relationship('ProfesorClase', back_populates='planificacion', cascade="all, delete-orphan")

    def __repr__(self):
        return '<planificacion: %r >' % (self.id_planificacion)

    def to_json(self):
        planificacion_json = {
            'id_planificacion': str(self.id_planificacion),
            'id_clase': self.id_clase,
            'horas_semanales': str(self.horas_semanales),
            'objetivo': str(self.objetivo),
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
