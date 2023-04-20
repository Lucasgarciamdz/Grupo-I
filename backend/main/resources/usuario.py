from flask_restful import Resource
from flask import request, jsonify
from .. import db, Usuario


class Usuarios(Resource):
    def get(self):
        usuarios = db.session.query(Usuario).all()
        return jsonify(usuario.to_json() for usuario in usuarios)

    def post(self):
        usuario = Usuario.from_json(request.get_json())
        db.session.add(usuario)
        db.session.commit()
        return usuario.to_json(), 201


class Usuario(Resource):
    def get(self, id):
        usuario = db.session.query(Usuario).get_or_404(id)
        return usuario.to_json()

    def put(self, id):
        usuario = db.session.query(Usuario).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(usuario, key, value)
        db.session.add(usuario)
        db.session.commit()
        return usuario.to_json(), 201

    def delete(self, id):
        usuario = db.session.query(Usuario).get_or_404(id)
        db.session.delete(usuario)
        db.session.commit()
        return '', 204