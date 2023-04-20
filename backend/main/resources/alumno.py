from flask_restful import Resource
from flask import request, jsonify
from .. import db
from .. import Alumno


class Alumnos(Resource):

    def get(self):
        alumnos = db.session.query(Alumno).all()
        return jsonify(alumno.to_json() for alumno in alumnos)

    def post(self):
        alumno = Alumno.from_json(request.get_json())
        db.session.add(alumno)
        db.session.commit()
        return alumno.to_json(), 201


class Alumno(Resource):

    def get(self, id):
        alumno = db.session.query(Alumno).get_or_404(id)
        return alumno.to_json()

    def put(self, id):
        alumno = db.session.query(alumno).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(alumno, key, value)
        db.session.add(alumno)
        db.session.commit()
        return alumno.to_json(), 201

    def delete(self, id):
        alumno = db.session.query(alumno).get_or_404(id)
        db.session.delete(alumno)
        db.session.commit()
        return '', 204
