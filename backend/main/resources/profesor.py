from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import ProfesorModel, ClasesModel, profesores_clases, PlanificacionModel, AlumnoModel
from sqlalchemy import desc, func


class Profesores(Resource):

    def get(self):

        profesores = db.session.query(ProfesorModel)
        page = 1

        per_page = 10

        if request.args.get('page'):
            page = int(request.args.get('page'))
        if request.args.get('per_page'):
            per_page = int(request.args.get('per_page'))

        # devuelve los profesores ordenados por sueldo de mayor a menor (NO ANDA O EL POSTMAN NO MUESTRA LAS COSAS ORDENADAS)
        if request.args.get('sort_by_sueldo'):
            profesores = profesores\
                        .order_by(desc(ProfesorModel.sueldo))

        # devuelve los profesores filtrados por estado
        if request.args.get('estado'):
            profesores = profesores\
                        .filter(ProfesorModel.estado.like(request.args.get('estado')))

        # devuelve los profesores con la cantidad de clases (chequear)
        if request.args.get('clases'):
            profes_id = db.session.query(ProfesorModel.id_profesor, ClasesModel.id_clase)
            primer_join = profes_id.join(profesores_clases, profesores_clases.id_profesor == ProfesorModel.id_profesor)
            segundo_join = primer_join.join(ClasesModel, ClasesModel.id_clase == profesores_clases.id_clase)
            profesores = segundo_join.order_by(ProfesorModel.id_profesor)

            """SELECT p.id_profesor, c.id_clase 
            FROM profesor p JOIN profesores_clases pc ON p.id_profesor = pc.id_profesor 
            JOIN clase c ON c.id_clase = pc.id_clase 
            ORDER BY p.id_profesor """

        # devuelve los profesores con sus alumnos (chequear)
        if request.args.get('alumnos'):
            query = db.session.query(ProfesorModel.id_profesor, AlumnoModel.id_alumno)\
                .join(Profesor.clases)\
                .join(ClasesModel.planificacion)\
                .join(PlanificacionModel.alumnos)\
                .join(AlumnoModel)\
                .all()
            
            """SELECT u.nombre, u.apellido, COUNT(a.id_alumno) AS cantidad_alumnos
            FROM usuario u JOIN profesor p ON u.id_usuario = p.id_usuario 
            JOIN profesores_clases pc ON p.id_profesor = pc.id_profesor
            JOIN clase c ON c.id_clase = pc.id_clase
            JOIN planificacion pl ON pl.id_clase  = c.id_clase 
            JOIN alumnos_planificaciones ap ON pl.id_planificacion = ap.id_planificacion 
            JOIN alumno a ON a.id_alumno = ap.id_alumno 
            GROUP BY u.nombre 
            ORDER BY u.nombre DESC"""

            result = [{'id_profesor': row[0], 'id_alumno': row[1]} for row in query]

            return jsonify(result)

        profesores = profesores.paginate(page=page, per_page=per_page, error_out=True, )

        return jsonify({"profesor": [profesor.to_json() for profesor in profesores],
                        "page": page,
                        "pages": profesores.pages,
                        "total": profesores.total
                        })

    def post(self):
        profesor = ProfesorModel.from_json(request.get_json())
        db.session.add(profesor)
        db.session.commit()
        return profesor.to_json(), 201


class Profesor(Resource):

    def get(self, id):
        profesor = db.session.query(ProfesorModel).get_or_404(id)
        return profesor.to_json()

    def put(self, id):
        profesor = db.session.query(ProfesorModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(profesor, key, value)
        db.session.add(profesor)
        db.sessiprofesormit()
        return profesor.to_json(), 201

    def delete():
        profesor = db.session.query(ProfesorModel).get_or_404(id)
        db.session.delete(profesor)
        db.session.commit()
        return '', 204
