from flask_restful import Resource
from flask import request

PLANIFICACIONES = {
    1: {"nombre": "Planificación 1", "descripcion": "Descripción 1", "alumno": "1", "profesor": "3", "estado": "Activa"},
    2: {"nombre": "Planificación 2", "descripcion": "Descripción 2", "profesor": "3", "estado": "Activa"},
    3: {"nombre": "Planificación 3", "descripcion": "Descripción 3", "alumno": "1", "estado": "Inactiva"},
}

def obtener_planificaciones_por_id(id):
    planificaciones = []
    for planificacion in PLANIFICACIONES.values():
        if planificacion.get("alumno") == id:
            planificaciones.append(planificacion)
    return planificaciones

def crear_planificacion(data):
    id = int(max(PLANIFICACIONES.keys()))+1
    PLANIFICACIONES[id] = data
    return PLANIFICACIONES[id]

def obtener_planificacion(id):
    if int(id) in PLANIFICACIONES:
        return PLANIFICACIONES[int(id)]
    return "", 404


class PlanificacionAlumno(Resource):
    def get(self, id):
        planificaciones = []
        for planificacion in PLANIFICACIONES.values():
            if planificacion.get("alumno") == id:
                planificaciones.append(planificacion)
        return planificaciones


class PlanificacionesAlumnos(Resource):
    def get(self):
        planificaciones = []
        for planificacion in PLANIFICACIONES.values():
            if planificacion.get("alumno"):
                planificaciones.append(planificacion)
        return planificaciones


class PlanificacionesProfesores(Resource):
    def get(self):
        planificaciones = []
        for planificacion in PLANIFICACIONES.values():
            if planificacion.get("profesor"):
                planificaciones.append(planificacion)
        return planificaciones

    def post(self):
        nueva_planificacion = request.get_json()
        id = int(max(PLANIFICACIONES.keys()))+1
        PLANIFICACIONES[id] = nueva_planificacion
        return PLANIFICACIONES[id], 201


class PlanificacionProfesor(Resource):
    def get(self, id):
        planificaciones = []
        for planificacion in PLANIFICACIONES.values():
            if planificacion.get("profesor") == id:
                planificaciones.append(planificacion)
        return planificaciones


    def put(self, id):
        planificacionid = []
        for planificacion in PLANIFICACIONES.values():
            if planificacion.get("profesor") == id:
                planificacionid.append(planificacion)
        data = request.get_json()
        planificacion.update(data)
        return "", 201

    def delete(self, id):
        planificacion = obtener_planificacion_por_id(id)
        if planificacion:
            del PLANIFICACIONES[int(id)]
            return "", 204
        return "", 404
