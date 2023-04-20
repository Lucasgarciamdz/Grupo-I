from .. import db


class Profesor(db.Model):

    __tablename__ = "profesor"

    id_profesor = db.Column(db.Integer, primary_key=True)
    certificacion = db.Column(db.String(45), nullable=False)
    fecha_inicio_actividad = db.Column(db.String(45), nullable=False)
    sueldo = db.Column(db.Float, nullable=False)
    estado = db.Column(db.String(45), nullable=False)
    # id_usuario = db.Column(db.Integer, db.ForeignKey('Usuario.id_usuario'))

    def __repr__(self):
        return '<profesor: %r >' % (self.id_profesor)

    def to_json(self):
        profesor_json = {
            'id_profesor': str(self.id_profesor),
            'certificacion': self.certificacion,
            'fecha_inicio_actividad': self.fecha_inicio_actividad,
            'sueldo': str(self.sueldo),
            'estado': self.estado,
            # 'id_usuario': self.id_usuario,

        }
        return profesor_json

    @staticmethod
    def from_json(profesor_json):
        id_profesor = profesor_json.get('id_profesor')
        certificacion = profesor_json.get('certificacion')
        fecha_inicio_actividad = profesor_json.get('fecha_inicio_actividad')
        sueldo = profesor_json.get('sueldo')
        estado = profesor_json.get('estado')
        # id_usuario = profesor_json.get('id_usuario')
        return Profesor(id_profesor=id_profesor,
                        certificacion=certificacion,
                        fecha_inicio_actividad=fecha_inicio_actividad,
                        sueldo=sueldo,
                        estado=estado,
                        # id_usuario=id_usuario
                        )
