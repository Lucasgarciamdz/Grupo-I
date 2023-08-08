from factory import db


class Clase(db.Model):

    __tablename__ = "clase"

    id_clase = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(45), nullable=False)

    planificacion = db.relationship('Planificacion', back_populates='clase', cascade="all, delete-orphan", single_parent=True)

    def __repr__(self):
        return '<clase: %r >' % (self.id_clase)

    def to_json(self):
        clase_json = {
            'id': str(self.id_clase),
            'nombre': self.nombre,
        }
        return clase_json

    def to_json_complete(self):
        clase_json = {
            'id': self.id_clase,
            'nombre': self.nombre,
            'planificacion': self.planificacion.to_json(),
            'profesores': [profesor.to_json() for profesor in self.profesores]
        }
        return clase_json

    @staticmethod
    def from_json(clase_json):
        id_clase = clase_json.get('id_clase')
        nombre = clase_json.get('nombre')
        return Clase(id_clase=id_clase,
                     nombre=nombre,
                     )
