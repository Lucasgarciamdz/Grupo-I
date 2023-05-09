from flask_restful import Resource
from .. import db
from flask import request, jsonify
from main.models import ClasesModel
from sqlalchemy import desc, func


class Clases(Resource):
    def get(self):
        clases = db.session.query(ClasesModel)

        page = 1

        per_page = 10

        if request.args.get('page'):
            page = int(request.args.get('page'))
        if request.args.get('per_page'):
            per_page = int(request.args.get('per_page'))

        # devuelve todas las planificaciones que tienen una determinada clase
        if request.args.get('clase'):
            clases = clases.join(ClasesModel.planificacion).filter_by(clases.tipo.like(request.args.get('clase')))
            
        # if request.args.get('sort_by_planificaciones'):
        #     clases = clases.join(ClasesModel.planificacion).group_by(ClasesModel.tipo).order_by(desc(func.count(ClasesModel.id_alumno)))
        
        try:
            clases = clases.paginate(page=page, per_page=per_page, error_out=True, )
        except:
            return jsonify({"error":"pasame bien las cositas amiguito"})
        
        return jsonify({"clase": [clase.to_json() for clase in clases],
                        "page": page,
                        "pages": clases.pages,
                        "total": clases.total
                        })

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
