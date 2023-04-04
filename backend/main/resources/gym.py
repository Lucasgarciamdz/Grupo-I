from flask_restful import Resource
from flask import request


USUARIOS = {
    1: {'nombre': 'Franco', 'apellido': 'Bertoldi''rol': 'alumno'},
    2: {'nombre': 'Francisco', 'apellido': 'Lopez Garcia''rol': 'alumno'}
    3: {'nombre': 'Franco', 'apellido': 'Bertoldi', 'rol': 'profesor'},
    4: {'nombre': 'Francisco', 'apellido': 'Lopez Garcia''rol': 'profesor'}

}

USUARIOS_ALUMNOS = {
    1: {'nombre': 'Franco', 'apellido': 'Bertoldi''rol': 'alumno'},
    2: {'nombre': 'Francisco', 'apellido': 'Lopez Garcia''rol': 'alumno'}
}

USUARIOS_PROFESORES = {
    1: {'nombre': 'Franco', 'apellido': 'Bertoldi', 'rol': 'profesor'},
    2: {'nombre': 'Francisco', 'apellido': 'Lopez Garcia''rol': 'profesor'}
}

PLANIFICACIONES = {
    1: {'nombre': 'Planificación 1', 'descripcion': 'Descripción 1', 'alumno': '1', 'profesor': '3', 'estado': 'Activa'},
    2: {'nombre': 'Planificación 2', 'descripcion': 'Descripción 2', 'alumno': '2', 'profesor': '3', 'estado': 'Activa'},
    3: {'nombre': 'Planificación 3', 'descripcion': 'Descripción 3', 'alumno': '1', 'profesor': '4', 'estado': 'Inactiva'},
}

PROFESORES_CLASES = {
    3: {'nombre': 'Franco', 'apellido': 'Bertoldi', 'clases': ['funcional']},
    4: {'nombre': 'Francisco', 'apellido': 'Lopez Garcia', 'clases': ['powerlifting']}
}

PAGOS = {
    1: {'alumno': '1', 'monto': '1000', 'estado': 'Pendiente'},
    2: {'alumno': '2', 'monto': '1500', 'estado': 'Pagado'},
}

def usuario_tiene_rol(user_id, rol):
    if user_id in USUARIOS:
        return USUARIOS[user_id].get('rol') == rol
    return False

def obtener_planificaciones_por_id(id):
    planificaciones = []
    for planificacion in PLANIFICACIONES.values():
        if planificacion.get('alumno') == id:
            planificaciones.append(planificacion)
    return planificaciones

def crear_planificacion(data):
    id = int(max(PLANIFICACIONES.keys()))+1
    PLANIFICACIONES[id] = data
    return PLANIFICACIONES[id]

def obtener_planificacion(id):
    if int(id) in PLANIFICACIONES:
        return PLANIFICACIONES[int(id)]
    return '', 404

def 

class Usuarios(Resource):
    def get(self):
        return USUARIOS

    def post(self):
        usuarios = request.get_json()
        id = int(max(USUARIOS.keys()))+1
        USUARIOS[id] = usuarios
        return USUARIOS[id], 201

class Usuario(Resource):
    def get(self, id):
        if int(id) in USUARIOS:
            return USUARIOS[int(id)]
        return '', 404

    def delete(self, id):
        if int(id) in USUARIOS:
            del USUARIOS[int(id)]
            return '', 204
        return '', 404

    def put(self, id):
        if int(id) in USUARIOS:
            usuario = USUARIOS[int(id)]
            data = request.get_json()
            usuario.update(data)
            return '', 201
        return '', 404


class UsuariosAlumnos(Resource):
    def get(self):
        return USUARIOS_ALUMNOS
    
    def post(self):
        usuarios_alumnos = request.get_json()
        id = int(max(USUARIOS_ALUMNOS.keys()))+1
        USUARIOS_ALUMNOS[id] = usuarios_alumnos
        return USUARIOS_ALUMNOS[id], 201

class UsuarioProfesor(Resource):
    def get(self, id):
        if int(id) in USUARIOS_PROFESORES:
            return USUARIOS_PROFESORES[int(id)]
        return '', 404

    def put(self, id):
        if int(id) in USUARIOS_PROFESORES:
            usuario_profesor = USUARIOS_PROFESORES[int(id)]
            data = request.get_json()
            usuario_profesor.update(data)
            return '', 201
        return '', 404        

class UsuarioAlumno(Resource):
    def get(self, id):
        if int(id) in USUARIOS_ALUMNOS:
            return USUARIOS_ALUMNOS[int(id)]
        return '', 404

    def put(self, id):
        # Validar que el usuario tenga rol de admin o profesor
        if usuario_tiene_rol(request.headers.get('Authorization'), ['admin', 'profesor']):
            if int(id) in USUARIOS_ALUMNOS:
                usuario_alumno = USUARIOS_ALUMNOS[int(id)]
                data = request.get_json()
                usuario_alumno.update(data)
                return '', 201
            return '', 404  
        return '', 401

    def delete(self, id):
        # Validar que el usuario tenga rol de admin o profesor
        if usuario_tiene_rol(request.headers.get('Authorization'), ['admin', 'profesor']):
            if int(id) in USUARIOS_ALUMNOS:
                del USUARIOS_ALUMNOS[int(id)]
                return '', 204
            return '', 404
        return '', 401


class PlanificacionAlumno(Resource):
    def get(self, id):
        # Validar que el usuario tenga rol de admin, profesor o alumno
        if usuario_tiene_rol(request.headers.get('Authorization'), ['admin', 'profesor', 'alumno']):
            # Obtener planificaciones por alumno
            planificaciones = obtener_planificaciones_por_alumno(id)
            return planificaciones
        return '', 401


class PlanificacionesProfesores(Resource):
    def get(self):
        # Validar que el usuario tenga rol de admin o profesor
        if usuario_tiene_rol(request.headers.get('Authorization'), ['admin', 'profesor']):
            # Obtener todas las planificaciones
            planificaciones = obtener_planificaciones()
            return planificaciones
        return '', 401

    def post(self):
        # Validar que el usuario tenga rol de admin o profesor
        if usuario_tiene_rol(request.headers.get('Authorization'), ['admin', 'profesor']):
            # Crear una nueva planificación
            nueva_planificacion = request.get_json()
            id = crear_planificacion(nueva_planificacion)
            return id, 201
        return '', 401


class PlanificacionProfesor(Resource):
    def get(self, id):
        # Validar que el usuario tenga rol de admin o profesor
        if usuario_tiene_rol(request.headers.get('Authorization'), ['admin', 'profesor']):
            # Obtener una planificación por id
            planificacion = obtener_planificacion_por_id(id)
            if planificacion:
                return planificacion
            return '', 404
        return '', 401

    def put(self, id):
        # Validar que el usuario tenga rol de admin o profesor
        if usuario_tiene_rol(request.headers.get('Authorization'), ['admin', 'profesor']):
            # Editar una planificación existente
            planificacion = obtener_planificacion_por_id(id)
            if planificacion:
                data = request.get_json()
                planificacion.update(data)
                return '', 201
            return '', 404
        return '', 401
    
    def delete(self, id):
        # Validar que el usuario tenga rol de admin o profesor
        if usuario_tiene_rol(request.headers.get('Authorization'), ['admin', 'profesor']):
            # Eliminar una planificación existente
            planificacion = obtener_planificacion_por_id(id)
            if planificacion:
                del PLANIFICACIONES[int(id)]
                return '', 204
            return '', 404
        return '', 401