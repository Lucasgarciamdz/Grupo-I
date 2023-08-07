from flask_restful import Resource
from flask import request, jsonify
from factory import db
from models.alumno_model import Alumno as AlumnoModel
from models.planificacion_model import Planificacion as PlanificacionModel
from models.usuario_model import Usuario as UsuarioModel
from sqlalchemy import func
from flask_jwt_extended import jwt_required
from auth.decoradores import role_required


class Alumnos(Resource):

    @jwt_required()
    def get(self):
        alumnos = db.session.query(AlumnoModel)

        page = 1
        per_page = 10

        if request.args.get('page'):
            page = int(request.args.get('page'))

        if request.args.get('per_page'):
            per_page = int(request.args.get('per_page'))

        # devuelve la cantidad de alumnos por cada estado posible (chequear)
        if request.args.get('estado'):
            alumnos = db.session.query(AlumnoModel.estado, func.count(AlumnoModel.id_alumno))\
                        .group_by(AlumnoModel.estado)

        # devuleve todos los alumnos que tienen la planilla medica vencida (NO ANDA)
        if request.args.get('planilla_medica_falso'):
            alumnos = alumnos.filter(not AlumnoModel.planilla_medica)

        try:
            alumnos = alumnos.paginate(page=page, per_page=per_page, error_out=True)
        except Exception:
            return jsonify({"error": "Error inesperado"})

        return jsonify({"alumnos": [alumno.to_json() for alumno in alumnos],
                        "page": page,
                        "pages": alumnos.pages,
                        "total": alumnos.total
                        })

    @jwt_required()
    def post(self):
        try:
            data = request.get_json()
        except Exception:
            return "Error al pasar a JSON"
        alumno = AlumnoModel.from_json(data["alumno"])
        if "planificacion" in data:
            try:
                planificacion = db.session.query(PlanificacionModel).filter(PlanificacionModel.nombre.like(data["planificacion"]["nombre"])).first()
                db.session.add(planificacion)
                planificacion.alumnos_p.append(alumno)
            except Exception:
                return f"no existe la planificacion {data['planificacion']['nombre']}"
        if "usuario" in data:
            try:
                usuario = db.session.query(UsuarioModel).filter(UsuarioModel.nombre.like(data["usuario"]["dni"])).first()
                alumno['id_usuario'] = usuario.id_usuario
            except Exception:
                return f"no existe el usuario dni {data['usuario']['dni']}"
        db.session.add(alumno)
        db.session.commit()
        return alumno.to_json()


class Alumno(Resource):

    @jwt_required(optional=True)
    def get(self, id):
        alumno = db.session.query(AlumnoModel).get_or_404(id)
        return alumno.to_json()

    @role_required('admin')
    def put(self, id):
        alumno = db.session.query(AlumnoModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(alumno, key, value)
        db.session.add(alumno)
        db.session.commit()
        return alumno.to_json(), 201

    @role_required(roles="admin")
    def delete(self, id):
        alumno = db.session.query(AlumnoModel).get_or_404(id)
        db.session.delete(alumno)
        db.session.commit()
        return '', 204
