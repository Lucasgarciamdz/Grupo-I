from flask import request, jsonify
from flask_jwt_extended import jwt_required
from flask_restful import Resource

from main.auth.decoradores import role_required
from main.mail.functions import sendMail
from main.models import PlanificacionModel, AlumnoModel
from .. import db


class Planificaciones(Resource):

    # @jwt_required()
    def get(self):

        planificaciones = db.session.query(PlanificacionModel)

        page = 1
        per_page = 10

        if request.args.get('page'):
            page = int(request.args.get('page'))
        if request.args.get('per_page'):
            per_page = int(request.args.get('per_page'))

        # devuelve una lista de planificaciones asociadas a un alumno
        if request.args.get('alumno_id_plani'):
            alumno_id = request.args.get('alumno_id_plani')
            alumno = AlumnoModel.query.filter_by(id_alumno=alumno_id).first()
            planificaciones = alumno.planificaciones

            planificaciones_json = [planificacion.to_json() for planificacion in planificaciones]

            return planificaciones_json

        # devuelve las planificaciones con determinado objetivo
        if request.args.get('objetivo'):
            planificaciones = planificaciones.filter(PlanificacionModel.objetivo.like(request.args.get('objetivo')))

        # #devuelve una lista ordenada de los alumnos que estan en esa planificacion (chequear)
        if request.args.get('sortby_planificacion'):
            alumnos = db.session.query(AlumnoModel) \
                .join(AlumnoModel.planificaciones) \
                .filter(PlanificacionModel.id_planificacion.like(request.args.get('sortby_planificacion'))) \
                .all()

            return jsonify({
                "alumno": [alumno.to_json() for alumno in alumnos],
                "page": page,
                "pages": planificaciones.pages,
                "total": planificaciones.total
            })

        try:
            planificaciones = planificaciones.paginate(page=page, per_page=per_page, error_out=True)
        except Exception:
            return jsonify({"error": "Error inesperado"})

        return jsonify({"planificacion": [planificacion.to_json() for planificacion in planificaciones],
                        "page": page,
                        "pages": planificaciones.pages,
                        "total": planificaciones.total
                        })

    @jwt_required()
    def post(self):
        try:
            planificacion = PlanificacionModel.from_json(request.get_json())
        except Exception:
            return "Error al pasar a JSON"
        alumnos = db.session.query(AlumnoModel)
        sendMail([alumno.email for alumno in alumnos], "Nueva planificacion!", 'planificacion_nueva',
                 planificacion=planificacion)
        db.session.add(planificacion)
        db.session.commit()
        return planificacion.to_json(), 201


class Planificacion(Resource):

    @jwt_required(optional=True)
    def get(self, id):
        planificacion = db.session.query(PlanificacionModel).get_or_404(id)
        return planificacion.to_json()

    @jwt_required()
    @role_required(roles=["Admin", "Alumno"])
    def put(self, id):
        planificacion = db.session.query(PlanificacionModel).get_or_404(id)

        if request.args.get('alumno_id_join'):
            alumno_id = request.args.get('alumno_id_join')
            alumno = db.session.query(AlumnoModel).get_or_404(alumno_id)
            planificacion.alumnos.append(alumno)
        else:
            data = request.get_json().items()
            for key, value in data:
                setattr(planificacion, key, value)
        
        if request.args.get('alumno_id_remove'):
            alumno_id = request.args.get('alumno_id_remove')
            alumno = db.session.query(AlumnoModel).get_or_404(alumno_id)
            planificacion.alumnos.remove(alumno)
        else:
            data = request.get_json().items()
            for key, value in data:
                setattr(planificacion, key, value)

        db.session.add(planificacion)
        db.session.commit()
        return planificacion.to_json(), 201

    @jwt_required()
    @role_required(roles="Admin")
    def delete(self, id):
        planificacion = db.session.query(PlanificacionModel).get_or_404(id)
        db.session.delete(planificacion)
        db.session.commit()
        return '', 204
