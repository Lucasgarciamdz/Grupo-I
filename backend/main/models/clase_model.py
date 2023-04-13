from .. import db


class Clase(db.Model):

    __tablename__ = "Clase"
    
    id_clase = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(45), nullable=False)

    def __repr__(self):
        return '<Clase: %r >' % (self.id_clase)

    def to_json(self):
        clase_json = {
            'id': self.id_clase,
            'tipo': self.tipo,

        }
        return clase_json
    
# que carajo hace esto
    def to_json_short(self):
        animal_json = {
            'id': self.id_clase,
            'tipo': self.tipo,

        }
        return animal_json

    @staticmethod
    def from_json(clase_json):
        id_clase = clase_json.get('id_clase')
        tipo = clase_json.get('tipo')
        return Clase(id=id_clase,
                        tipo=tipo
                        )
