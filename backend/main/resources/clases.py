from flask_restful import Resource


PROFESORES_CLASES = {
    1: {'nombre': 'Franco', 'apellido': 'Bertoldi', 'clases': ['funcional']},
    2: {'nombre': 'Francisco', 'apellido': 'Lopez Garcia', 'clases': ['powerlifting']}
}


class ProfesoresClases(Resource):
    def get(self):
        return PROFESORES_CLASES


class ProfesorClases(Resource):
    def get(self, id):
        if int(id) in PROFESORES_CLASES:
            return PROFESORES_CLASES[int(id)]
        return '', 404
