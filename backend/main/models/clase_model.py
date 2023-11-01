from .. import db
from .profesor_model import profesores_clases


class Clase(db.Model):

    __tablename__ = "clase"

    id_clase = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(45))
    descripcion = db.Column(db.String(45))
    imagen = db.Column(db.String(45))

    planificacion = db.relationship('Planificacion', back_populates='clase', cascade="all, delete-orphan", single_parent=True)
    profesores = db.relationship('Profesor', secondary=profesores_clases, backref=db.backref('clases_p', lazy='dynamic'), overlaps="clases,profesores_p")

    def __repr__(self):
        return '<clase: %r >' % (self.id_clase)

    def to_json(self):
        clase_json = {
            'id': str(self.id_clase),
            'tipo': self.tipo,
            'descripcion': self.descripcion,
            'imagen': self.imagen
        }
        return clase_json

    def to_json_complete(self):
        clase_json = {
            'id': self.id_clase,
            'tipo': self.tipo,
            'desscripcion': self.descripcion,
            'imagen': self.imagen,
            'planificacion': self.planificacion.to_json(),
            'profesores': [profesor.to_json() for profesor in self.profesores]
        }
        return clase_json

    @staticmethod
    def from_json(clase_json):
        id_clase = clase_json.get('id_clase')
        tipo = clase_json.get('tipo')
        descripcion = clase_json('descripcion')
        imagen = clase_json('imagen')
        return Clase(id_clase=id_clase,
                     tipo=tipo,
                     descripcion=descripcion,
                     imagen=imagen
                     )
