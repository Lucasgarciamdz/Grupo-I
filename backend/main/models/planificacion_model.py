from .. import db


class Planificacion(db.Model):

    __tablename__ = "planificacion"

    id_planificacion = db.Column(db.Integer, primary_key=True)
    horas_semanales = db.Column(db.Integer)
    objetivo = db.Column(db.String(45))
    # id_clase = db.Column(db.String(45), db.ForeignKey('Clase.id_clase'))

    def __repr__(self):
        return '<planificacion: %r >' % (self.id_planificacion)

    def to_json(self):
        planificacion_json = {
            'id_planificacion': str(self.id_planificacion),
            'horas_semanales': str(self.horas_semanales),
            'objetivo': str(self.objetivo),
            # 'id_clase': self.id_clase,
        }
        return planificacion_json

    @staticmethod
    def from_json(planificacion_json):
        id_planificacion = planificacion_json.get('id_planificacion')
        horas_semanales = planificacion_json.get('horas_semanales')
        objetivo = planificacion_json.get('objetivo')
        # id_clase = planificacion_json.get('id_clase')
        return Planificacion(id_planificacion=id_planificacion,
                             horas_semanales=horas_semanales,
                             objetivo=objetivo,
                             # id_clase=id_clase
                             )