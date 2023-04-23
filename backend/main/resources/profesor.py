from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import ProfesorModel


class Profesores(Resource):

    def get(self):
        profesores = db.session.query(ProfesorModel).all()
        profesor_json = [profesor.to_json() for profesor in profesores]
        return jsonify(profesor_json)

    def post(self):
        profesor = ProfesorModel.from_json(request.get_json())
        db.session.add(profesor)
        db.session.commit()
        return profesor.to_json(), 201


class Profesor(Resource):

    def get(self, id):
        profesor = db.session.query(ProfesorModel).get_or_404(id)
        return profesor.to_json()

    def put(self, id):
        profesor = db.session.query(ProfesorModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(profesor, key, value)
        db.session.add(profesor)
        db.sessiprofesormit()
        return profesor.to_json(), 201

    def delete():
        profesor = db.session.query(ProfesorModel).get_or_404(id)
        db.session.delete(profesor)
        db.session.commit()
        return '', 204
