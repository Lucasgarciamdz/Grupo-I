from flask_restful import Resource
from .. import db
from flask import request, jsonify
from main.models import ClasesModel


class Clases(Resource):
    def get():
        clases = db.session.query(ClasesModel).all()
        clase_json = [clase.to_json() for clase in clases]
        return jsonify(clase_json)

    def post(self):
        clase = ClasesModel.from_json(request.get_json())
        db.session.add(clase)
        db.session.commit()
        return clase.to_json(), 201


class Clase(Resource):
    def get(self, id):
        clase = db.session.query(ClasesModel).get_or_404(id)
        return clase.to_json()

    def put(self, id):
        clase = db.session.query(ClasesModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(clase, key, value)
        db.session.add(clase)
        db.session.commit()
        return clase.to_json(), 201

    def delete(self, id):
        clase = db.session.query(ClasesModel).get_or_404(id)
        db.session.delete(clase)
        db.session.commit()
        return '', 204
