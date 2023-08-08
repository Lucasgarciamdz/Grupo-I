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

    def __repr__(self):
        return '<alumno: %r >' % (self.id_alumno)

    def to_json(self):
        """Return a JSON representation of the Alumno object."""
        alumno_json = {
            'id_alumno': self.id_alumno,
            'estado': self.estado,
            'planilla_medica': self.planilla_medica,
        }
        return alumno_json

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

    @staticmethod
    def from_json(alumno_json):
        """Create an Alumno object from a JSON representation."""
        id_alumno = alumno_json.get('id_alumno', None)
        id_usuario = alumno_json.get('id_usuario', None)
        estado = alumno_json.get('estado', None)
        planilla_medica = alumno_json.get('planilla_medica', None)
        return Alumno(id_alumno=id_alumno,
                      id_usuario=id_usuario,
                      estado=estado,
                      planilla_medica=planilla_medica,
                      )
