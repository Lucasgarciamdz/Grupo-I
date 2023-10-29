from flask_restful import Resource
from .. import db
from flask import request, jsonify
from main.models import ClasesModel
from flask_jwt_extended import jwt_required
from main.auth.decoradores import role_required


class Clases(Resource):

    # @jwt_required()
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

        try:
            clases = clases.paginate(page=page, per_page=per_page, error_out=True)
        except Exception:
            return jsonify({"clase": []})

        return jsonify({"clase": [clase.to_json() for clase in clases],
                        "page": page,
                        "pages": clases.pages,
                        "total": clases.total
                        })

    # @jwt_required()
    def post(self):
        try:
            clase = ClasesModel.from_json(request.get_json())
        except Exception:
            return "Error al pasar a JSON"
        db.session.add(clase)
        db.session.commit()
        return clase.to_json(), 201


class Clase(Resource):

    @jwt_required(optional=True)
    def get(self, id):
        clase = db.session.query(ClasesModel).get_or_404(id)
        return clase.to_json()

    @role_required(roles="admin")
    def put(self, id):
        clase = db.session.query(ClasesModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(clase, key, value)
        db.session.add(clase)
        db.session.commit()
        return clase.to_json(), 201

    @role_required(roles="admin")
    def delete(self, id):
        clase = db.session.query(ClasesModel).get_or_404(id)
        db.session.delete(clase)
        db.session.commit()
        return '', 204
