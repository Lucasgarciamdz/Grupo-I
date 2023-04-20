from flask_restful import Resource
from flask import request, jsonify
from .. import db
from .. import Prof


class Profesores(Resource):

    def get(self, id):
        profesor = db.session.query(Profesor).get_or_404(id)
        return profesor.to_json()

    def post(self):
        profesor = Profesor.from_json(request.get_json())
        db.session.add(profesor)
        db.session.commit()
        return profesor.to_json(), 201


class Profesor(Resource):
    def get(self):
        profesores = db.session.query(Profesor).all()
        return jsonify(profesor.to_json() for profesor in profesores)

    def put(self, id):
        profesor = db.session.query(profesor).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(profesor, key, value)
        db.session.add(profesor)
        db.sessiprofesormit()
        return profesor.to_json(), 201

    def delete():
        profesor = db.session.query(profesor).get_or_404(id)
        db.session.delete(profesor)
        db.session.commit()
        return '', 204