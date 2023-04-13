from .. import db


class Alumno(db.Model):
    id_alumno = db.Column(db.Integer, primary_key=True)
    estado = db.Column(db.String(45), nullable=False)
    planilla_medica = db.Column(db.Binary, nullable=False)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario'))

    def __repr__(self):
        return '<Animal: %r >' % (self.raza)

    def to_json(self):
        animal_json = {
            'id': self.id,
            'raza': str(self.raza),

        }
        return animal_json

    def to_json_short(self):
        animal_json = {
            'id': self.id,
            'raza': str(self.raza),

        }
        return animal_json

    @staticmethod
    def from_json(animal_json):
        id = animal_json.get('id')
        raza = animal_json.get('raza')
        return Gimnasio(id=id,
                        raza=raza,
                        )
