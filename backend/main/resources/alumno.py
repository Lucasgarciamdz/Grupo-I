from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import AlumnoModel


class Alumnos(Resource):

    def get(self):
        alumnos = db.session.query(AlumnoModel).all()
        alumno_json = [alumno.to_json() for alumno in alumnos]
        return jsonify(alumno_json)

    def post(self):
        alumno = AlumnoModel.from_json(request.get_json())
        db.session.add(alumno)
        db.session.commit()
        return alumno.to_json(), 201


class Alumno(Resource):

    def get(self, id):
        alumno = db.session.query(AlumnoModel).get_or_404(id)
        return alumno.to_json()

    def put(self, id):
        alumno = db.session.query(AlumnoModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(alumno, key, value)
        db.session.add(alumno)
        db.session.commit()
        return alumno.to_json(), 201

    def delete(self, id):
        alumno = db.session.query(AlumnoModel).get_or_404(id)
        db.session.delete(alumno)
        db.session.commit()
        return '', 204
