# from .. import db


# class ProfesorClase(db.Model):

#     __tablename__ = "profesor_clase"
    
#     id_profesor_clase = db.Column(db.Integer, primary_key=True)
#     id_clase = db.Column(db.Integer, db.ForeignKey('Clase.id_clase'))
#     id_profesor = db.Column(db.Integer, db.ForeignKey('Profesor.id_profesor'))

#     def __repr__(self):
#         return '<ProfesorClase: %r >' % (self.id_profesor_clase)

#     def to_json(self):
#         profesor_clase_json = {
#             'id_profesor_clase': self.id_profesor_clase,
#             'id_clase': self.id_clase,
#             'id_profesor': self.id_profesor,
    
#         }
#         return profesor_clase_json

#     @staticmethod
#     def from_json(profesor_clase_json):
#         id_profesor_clase = profesor_clase_json.get('id_profesor_clase')
#         id_clase = profesor_clase_json.get('id_clase')
#         id_profesor = profesor_clase_json.get('id_profesor')
#         return ProfesorClase(id=id_profesor_clase,
#                         id_clase=id_clase,
#                         id_profesor=id_profesor
#                         )
