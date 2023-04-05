from flask_restful import Resource
from flask import request

USUARIOS_PROFESORES = {
    1: {'nombre': 'Franco', 'apellido': 'Bertoldi', 'rol': 'profesor'},
    2: {'nombre': 'Francisco', 'apellido': 'Lopez Garcia', 'rol': 'profesor'}
}

class UsuarioProfesor(Resource):
    def get(self, id):
        if int(id) in USUARIOS_PROFESORES:
            return USUARIOS_PROFESORES[int(id)]
        return '', 404

    def put(self, id):
        if int(id) in USUARIOS_PROFESORES:
            usuario_profesor = USUARIOS_PROFESORES[int(id)]
            data = request.get_json()
            usuario_profesor.update(data)
            return '', 201
        return '', 404  

class UsuariosProfesores(Resource):
    def get(self):
        return USUARIOS_PROFESORES
    
    def post(self):
        usuarios_profesores = request.get_json()
        id = int(max(USUARIOS_PROFESORES.keys()))+1
        USUARIOS_PROFESORES[id] = usuarios_profesores
        return USUARIOS_PROFESORES[id], 201