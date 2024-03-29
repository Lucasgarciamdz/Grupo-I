from flask_restful import Resource
from .. import db
from flask import request, jsonify
from main.models import ClasesModel
from main.models import AlumnoModel
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
        
        if request.args.get('alumno_id_clase'):

            alumno_id = request.args.get('alumno_id_clase')

            alumno = AlumnoModel.query.filter_by(id_alumno=alumno_id).first()

            planificaciones = alumno.planificaciones

            clases = []
            for planificacion in planificaciones:
                clase = planificacion.clase
                if clase is not None:
                    clases.append(clase)

            clases_json = [clase.to_json() for clase in clases]

            return clases_json

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
        if request.args.get('planificaciones'):
            clase = db.session.query(ClasesModel).get_or_404(id)
            planificaciones = clase.planificacion
            return jsonify({"clase":clase.to_json(),
            "planificaciones": [planificacion.to_json() for planificacion in planificaciones]})

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
