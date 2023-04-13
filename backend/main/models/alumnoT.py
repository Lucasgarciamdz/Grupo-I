from .. import db


class Alumno(db.Model):

    def __init__(self, id_alumno = db.Column(db.Integer, primary_key=True), estado = db.Column(db.String(45), nullable=False), planilla_medica = db.Column(db.Binary, nullable=False), id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario'))):
        
        self.id_alumno = id_alumno
        self.estado = estado
        self.planilla_medica = planilla_medica
        self.id_usuario = id_usuario
        
    def __repr__(self):
        return '<Alumno: %r >' % (self.id_alumno)

    def to_json(self):
        animal_json = {
            'id': self.id_alumno,
            'estado': self.estado,
            'planilla medica': self.planilla_medica,
            'id usuario': self.id_usuario

        }
        return animal_json
    
# que carajo hace esto
    def to_json_short(self):
        animal_json = {
            'id': self.id,
            'raza': str(self.raza),

        }
        return animal_json

    @staticmethod
    def from_json(alumno_json):
        id_alumno = alumno_json.get('id_alumno')
        estado = alumno_json.get('estado')
        planilla_medica = alumno_json.get('planilla_medica')
        id_usuario = alumno_json.get('id_usuario')
        return Alumno(id=id_alumno,
                        estado=estado,
                        planilla_medica=planilla_medica,
                        id_usuario=id_usuario
                        )
