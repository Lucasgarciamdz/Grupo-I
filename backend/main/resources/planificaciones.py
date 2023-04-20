from flask_restful import Resource
from flask import request, jsonify
from .. import db, Planificacion

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
#         planificacion = db.session.query(Planificacion).get_or_404(id)
#         return planificacion.to_json()


# class PlanificacionesAlumnos(Resource):
#     def get(self):
#         planificaciones = db.session.query(Planificacion).all()
#         return jsonify(planificacion.to_json() for planificacion in planificaciones)


class Planificaciones(Resource):
    def get(self):
        planificaciones = db.session.query(Planificaciones).all()
        return jsonify(planificacion.to_json() for planificacion in planificaciones)

    def post(self):
        planificacion = Planificacion.from_json(request.get_json())
        db.session.add(planificacion)
        db.session.commit()
        return planificacion.to_json(), 201


class Planificacion(Resource):
    def get(self, id):
        planificacion = db.session.query(Planificacion).get_or_404(id)
        return planificacion.to_json()

    def put(self, id):
        planificacion = db.session.query(Planificacion).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(planificacion, key, value)
        db.session.add(planificacion)
        db.session.commit()
        return planificacion.to_json(), 201

    def delete(self, id):
        planificacion = db.session.query(Planificacion).get_or_404(id)
        db.session.delete(planificacion)
        db.session.commit()
        return '', 204