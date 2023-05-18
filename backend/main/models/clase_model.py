from .. import db
from .profesor_model import profesores_clases


class Clase(db.Model):

    __tablename__ = "clase"

    id_clase = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(45), nullable=False)

    planificacion = db.relationship('Planificacion', back_populates='clase', cascade="all, delete-orphan", single_parent=True)
    profesores = db.relationship('Profesor', secondary=profesores_clases, backref=db.backref('clases_p', lazy='dynamic'))

    def __repr__(self):
        return '<clase: %r >' % (self.id_clase)

    def to_json(self):
        clase_json = {
            'id': str(self.id_clase),
            'tipo': self.tipo,
        }
        return clase_json

    def to_json_complete(self):
        clase_json = {
            'id': self.id_clase,
            'tipo': self.tipo,
            'planificacion': self.planificacion.to_json(),
            'profesores': [profesor.to_json() for profesor in self.profesores]
        }
        return clase_json

    @staticmethod
    def from_json(clase_json):
        id_clase = clase_json.get('id_clase')
        tipo = clase_json.get('tipo')
        return Clase(id_clase=id_clase,
                     tipo=tipo,
                     )
