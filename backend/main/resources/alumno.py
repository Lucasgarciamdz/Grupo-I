from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import AlumnoModel, PlanificacionModel, ClaseModel  # Agrega los modelos necesarios
from sqlalchemy import func
from flask_jwt_extended import jwt_required
from main.auth.decoradores import role_required

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

        if request.args.get('estado'):
            alumnos = db.session.query(AlumnoModel.estado, func.count(AlumnoModel.id_alumno)).group_by(AlumnoModel.estado)

        if request.args.get('planilla_medica_falso'):
            # Filtra los alumnos que no tienen planilla médica válida
            alumnos = alumnos.filter(AlumnoModel.planilla_medica.is_(False))

        try:
            alumnos = alumnos.paginate(page=page, per_page=per_page, error_out=True)
        except Exception:
            return jsonify({"error": "Error inesperado"})

        return jsonify({"alumnos": [alumno.to_json_complete() for alumno in alumnos],
                        "page": page,
                        "pages": alumnos.pages,
                        "total": alumnos.total
                        })

    @jwt_required()
    def post(self):
        try:
            alumno = AlumnoModel.from_json(request.get_json())
        except Exception:
            return "Error al pasar a JSON"
        db.session.add(alumno)
        db.session.commit()
        return alumno.to_json(), 201

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

    @app.route('/clases_asociadas/<int:id_alumno>')
    def obtener_clases_asociadas(id_alumno):
        # Obtiene el alumno por ID
        alumno = db.session.query(AlumnoModel).get_or_404(id_alumno)
        
        # Obtiene las planificaciones asociadas al alumno
        planificaciones = db.session.query(PlanificacionModel).filter(PlanificacionModel.alumnos.contains(alumno)).all()
        clases_asociadas = []

        # Recorre las planificaciones y obtén las clases asociadas a cada una
        for planificacion in planificaciones:
            clase = db.session.query(ClaseModel).filter(ClaseModel.id_clase == planificacion.id_clase).first()
            if clase:
                clases_asociadas.append(clase.to_json())

        return jsonify({"clases_asociadas": clases_asociadas})
