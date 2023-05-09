from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import PlanificacionModel, AlumnoModel
from sqlalchemy import func, desc, text

# def obtener_planificaciones_por_id(id):
#     planificaciones = []
#     for planificacion in PLANIFICACIONES.values():
#         if planificacion.get("alumno") == id:
#             planificaciones.append(planificacion)
#     return planificaciones


# def crear_planificacion(data):
#     id = int(max(PLANIFICACIONES.keys()))+1
#     PLANIFICACIONES[id] = data
#     return PLANIFICACIONES[id]


# def obtener_planificacion(id):
#     if int(id) in PLANIFICACIONES:
#         return PLANIFICACIONES[int(id)]
#     return "", 404


# class PlanificacionAlumno(Resource):
#     def get(self, id):
#         planificacion = db.session.query(PlanificacionModel).get_or_404(id)
#         return planificacion.to_json()


# class PlanificacionesAlumnos(Resource):
#     def get(self):
#         planificaciones = db.session.query(PlanificacionModel).all()
#         return jsonify(planificacion.to_json() for planificacion in planificaciones)


class Planificaciones(Resource):

    def get(self):  

        planificaciones = db.session.query(PlanificacionModel)

        page = 1

        per_page = 10

        if request.args.get('page'):
            page = int(request.args.get('page'))
        if request.args.get('per_page'):
            per_page = int(request.args.get('per_page'))
        
        #devuelve las planificaciones con determinado objetivo
        if request.args.get('objetivo'):
            planificaciones = planificaciones.filter(PlanificacionModel.objetivo.like(request.args.get('objetivo')))
        
        # #devuelve una lista ordenada de los alumnos que estan en esa planificacion
        # if request.args.get('sortby_planificacion'):
        #     planificaciones = planificaciones.order_by(desc(PlanificacionModel.id_planificacion))

        # if request.args.get('sortby_planificacion'):
        #     planificaciones = PlanificacionModel.query.order_by(desc(PlanificacionModel.id_planificacion))
        #     alumnos = AlumnoModel.query.join(AlumnoModel.planificaciones).filter(PlanificacionModel.in_(planificaciones))

        # if request.args.get('sortby_planificacion'):
        #     planificaciones = planificaciones.innerjoin(PlanificacionModel.alumnos).order_by(desc(PlanificacionModel.id_planificacion))
        
        try:
            planificaciones = planificaciones.paginate(page=page, per_page=per_page, error_out=True, )
        except:
            return jsonify({"error":"Error inesperado"})
        
        return jsonify({"planificacion": [planificacion.to_json() for planificacion in planificaciones],
                        "page": page,
                        "pages": planificaciones.pages,
                        "total": planificaciones.total
                        })

    def post(self):
        planificacion = PlanificacionModel.from_json(request.get_json())
        db.session.add(planificacion)
        db.session.commit()
        return planificacion.to_json(), 201


class Planificacion(Resource):
    def get(self, id):
        planificacion = db.session.query(PlanificacionModel).get_or_404(id)
        return planificacion.to_json()

    def put(self, id):
        planificacion = db.session.query(PlanificacionModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(planificacion, key, value)
        db.session.add(planificacion)
        db.session.commit()
        return planificacion.to_json(), 201

    def delete(self, id):
        planificacion = db.session.query(PlanificacionModel).get_or_404(id)
        db.session.delete(planificacion)
        db.session.commit()
        return '', 204
