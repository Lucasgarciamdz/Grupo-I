# from .. import db


# class AlumnoPlanificacion(db.Model):

#     __tablename__ = "alumno_planificacion"
    
#     id_alumno_planificacion = db.Column(db.Integer, primary_key=True)
#     id_alumno = db.Column(db.Integer, db.ForeignKey('Alumno.id_alumno'))
#     id_planificacion = db.Column(db.Integer, db.ForeignKey('Planificacion.id_planificacion'))

#     def __repr__(self):
#         return '<Alumno: %r >' % (self.id_alumno)

#     def to_json(self):
#         alumno_planificacion_json = {
#             'id_alumno_planificacion': self.id_alumno_planificacion,
#             'id_alumno': self.id_alumno,
#             'id_planificacion': self.id_planificacion,

#         }
#         return alumno_planificacion_json

#     @staticmethod
#     def from_json(alumno_planificacion_json):
#         id_alumno_planificacion = alumno_planificacion_json.get('id_alumno_planificacion')
#         id_alumno = alumno_planificacion_json.get('id_alumno')
#         id_planificacion = alumno_planificacion_json.get('id_planificacion')
#         return AlumnoPlanificacion(id=id_alumno_planificacion,
#                         id_alumno=id_alumno,
#                         id_planificacion=id_planificacion
#                         )
