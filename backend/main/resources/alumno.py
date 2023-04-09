from flask_restful import Resource
from flask import request

USUARIOS_ALUMNOS = {
    1: {'nombre': 'Franco', 'apellido': 'Bertoldi', 'rol': 'alumno'},
    2: {'nombre': 'Francisco', 'apellido': 'Lopez Garcia', 'rol': 'alumno'}
}


class UsuariosAlumnos(Resource):
    def get(self):
        return USUARIOS_ALUMNOS

    def post(self):
        usuarios_alumnos = request.get_json()
        id = int(max(USUARIOS_ALUMNOS.keys()))+1
        USUARIOS_ALUMNOS[id] = usuarios_alumnos
        return USUARIOS_ALUMNOS[id], 201


class UsuarioAlumno(Resource):
    def get(self, id):
        if int(id) in USUARIOS_ALUMNOS:
            return USUARIOS_ALUMNOS[int(id)]
        return '', 404

    def put(self, id):
        # Validar que el usuario tenga rol de admin o profesor
        if int(id) in USUARIOS_ALUMNOS:
            usuario_alumno = USUARIOS_ALUMNOS[int(id)]
            data = request.get_json()
            usuario_alumno.update(data)
            return '', 201
        return '', 404

    def delete(self, id):
        if int(id) in USUARIOS_ALUMNOS:
            del USUARIOS_ALUMNOS[int(id)]
            return '', 204
        return '', 404
