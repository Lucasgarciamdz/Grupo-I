from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import ProfesorModel, ClasesModel, UsuarioModel
from sqlalchemy import desc, func, asc


class Profesores(Resource):

    def get(self):
        
        profesores = db.session.query(ProfesorModel)

        page = 1

        per_page = 10

        if request.args.get('page'):
            page = int(request.args.get('page'))
        if request.args.get('per_page'):
            per_page = int(request.args.get('per_page'))
        
        # devuelve los profesores ordenados por sueldo de mayor a menor (NO ANDA O EL POSTMAN NO MUESTRA LAS COSAS ORDENADAS)
        if request.args.get('sort_by_sueldo'):
            profesores = profesores\
                        .order_by(desc(ProfesorModel.sueldo))

        # devuelve los profesores filtrados por estado
        if request.args.get('estado'):
            profesores = profesores\
                        .filter(ProfesorModel.estado.like(request.args.get('estado')))

        # devuelve los profesores con la cantidad de clases (chequear)
        if request.args.get('clases'):
            profesores = db.session.query(ProfesorModel.id_profesor, func.count(ClasesModel.id_clase))\
                        .join(ProfesorModel)\
                        .join(ClasesModel)\
                        .group_by(ProfesorModel.id_profesor)\
                        .order_by(ProfesorModel.id_profesor)

        # devuelve los profesores con sus alumnos (chequear)
        if request.args.get('alumnos'):
            profesores = profesores.join(ProfesorModel.clases)\
                        .join(ClasesModel.alumnos)\
                        .group_by(ProfesorModel.id)\
                        .order_by(func.count(ClasesModel.alumnos).desc())

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
