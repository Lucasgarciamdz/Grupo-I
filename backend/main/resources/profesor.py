from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import ProfesorModel


class Profesores(Resource):

    def get(self):
        
        profesores = db.session.query(ProfesorModel)

        page = 1

        per_page = 10

        if request.args.get('page'):
            page = int(request.args.get('page'))
        if request.args.get('per_page'):
            per_page = int(request.args.get('per_page'))
        try:
            profesores = profesores.paginate(page=page, per_page=per_page, error_out=True, )
        except:
            return jsonify({"error":"pasame bien las cositas amiguito"})
        
        return jsonify({"profesor": [profesor.to_json() for profesor in profesores],
                        "page": page,
                        "pages": profesores.pages,
                        "total": profesores.total
                        })

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
