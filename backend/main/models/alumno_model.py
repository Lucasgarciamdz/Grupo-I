from .. import db


class Alumno(db.Model):

    __tablename__ = "alumno"

    id_alumno = db.Column(db.Integer, primary_key=True)
    estado = db.Column(db.String(45), nullable=False)
    planilla_medica = db.Column(db.Boolean, nullable=False)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'))
    usuario = db.relationship('Usuario', back_populates='alumno', use_list=False, cascade="all, delete-orphan", single_parent=True)
    alumno_planificacion = db.relationship('AlumnoPlanificacion', back_populates='alumno', cascade="all, delete-orphan")

    def __repr__(self):
        return '<alumno: %r >' % (self.id_alumno)

    def to_json(self):
        alumno_json = {
            'id': str(self.id_alumno),
            'estado': self.estado,
            'planilla medica': self.planilla_medica,
            # 'id usuario': self.id_usuario

        }
        return alumno_json

    @staticmethod
    def from_json(alumno_json):
        id_alumno = alumno_json.get('id_alumno')
        estado = alumno_json.get('estado')
        planilla_medica = alumno_json.get('planilla_medica')
        # id_usuario = alumno_json.get('id_usuario')
        return Alumno(id_alumno=id_alumno,
                      estado=estado,
                      planilla_medica=planilla_medica,
                      # id_usuario=id_usuario
                      )
