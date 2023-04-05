from flask_restful import Resource
from flask import request

USUARIOS = {
    1: {'nombre': 'Franco', 'apellido': 'Bertoldi','rol': 'alumno'},
    2: {'nombre': 'Francisco', 'apellido': 'Lopez Garcia', 'rol': 'alumno'},
    3: {'nombre': 'Franco', 'apellido': 'Bertoldi', 'rol': 'profesor'},
    4: {'nombre': 'Francisco', 'apellido': 'Lopez Garcia', 'rol': 'profesor'}

}

class Usuarios(Resource):
    def get(self):
        return USUARIOS

    def post(self):
        usuarios = request.get_json()
        id = int(max(USUARIOS.keys()))+1
        USUARIOS[id] = usuarios
        return USUARIOS[id], 201

class Usuario(Resource):
    def get(self, id):
        if int(id) in USUARIOS:
            return USUARIOS[int(id)]
        return '', 404

    def delete(self, id):
        if int(id) in USUARIOS:
            del USUARIOS[int(id)]
            return '', 204
        return '', 404

    def put(self, id):
        if int(id) in USUARIOS:
            usuario = USUARIOS[int(id)]
            data = request.get_json()
            usuario.update(data)
            return '', 201
        return '', 404