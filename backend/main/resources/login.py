from flask_restful import Resource
from flask import request

LOGIN = {
    1: {'nombre': 'Franco', 'apellido': 'Bertoldi','rol': 'admin'}, 
}

class Login(Resource):
    def post(self):
        nuevo_usuarios = request.get_json()
        id = int(max(LOGIN.keys()))+1
        LOGIN[id] = nuevo_usuarios
        return LOGIN[id], 201