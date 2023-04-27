from .. import db


class Profesor(db.Model):

    __tablename__ = "profesor"

    id_profesor = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'))

    certificacion = db.Column(db.String(45), nullable=False)
    fecha_inicio_actividad = db.Column(db.String(45), nullable=False)
    sueldo = db.Column(db.Float, nullable=False)
    estado = db.Column(db.String(45), nullable=False)

    usuario = db.relationship('Usuario', back_populates='profesor', use_list=False, cascade="all, delete-orphan", single_parent=True)
    profesor_clase = db.relationship('ProfesorClase', back_populates='profesor', cascade="all, delete-orphan")

    def __repr__(self):
        return '<profesor: %r >' % (self.id_profesor)

    def to_json(self):
        profesor_json = {
            'id_profesor': str(self.id_profesor),
            'id_usuario': self.id_usuario,
            'certificacion': self.certificacion,
            'fecha_inicio_actividad': self.fecha_inicio_actividad,
            'sueldo': str(self.sueldo),
            'estado': self.estado,

        }
        return profesor_json

    @staticmethod
    def from_json(profesor_json):
        id_profesor = profesor_json.get('id_profesor')
        id_usuario = profesor_json.get('id_usuario')
        certificacion = profesor_json.get('certificacion')
        fecha_inicio_actividad = profesor_json.get('fecha_inicio_actividad')
        sueldo = profesor_json.get('sueldo')
        estado = profesor_json.get('estado')
        return Profesor(id_profesor=id_profesor,
                        id_usuario=id_usuario,
                        certificacion=certificacion,
                        fecha_inicio_actividad=fecha_inicio_actividad,
                        sueldo=sueldo,
                        estado=estado,
                        )
