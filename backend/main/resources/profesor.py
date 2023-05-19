from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import ProfesorModel, ClasesModel
from sqlalchemy import desc, func
from flask_jwt_extended import jwt_required
from main.auth.decoradores import role_required


class Profesores(Resource):

    @jwt_required()
    def get(self):
        profesores = db.session.query(ProfesorModel)
        page = 1
        per_page = 1

        if request.args.get('page'):
            page = int(request.args.get('page'))

        if request.args.get('per_page'):
            per_page = int(request.args.get('per_page'))

        # devuelve los profesores ordenados por sueldo de mayor a menor (NO ANDA O EL POSTMAN NO MUESTRA LAS COSAS ORDENADAS)
        if request.args.get('sort_by_sueldo'):
            profesores = profesores.order_by(desc(ProfesorModel.sueldo))

        # devuelve los profesores filtrados por estado
        if request.args.get('estado'):
            profesores = profesores.filter(ProfesorModel.estado.like(request.args.get('estado')))

        # devuelve los profesores con la cantidad de clases (chequear)
        if request.args.get('clases'):
            page = request.args.get('page', 1, type=int)
            per_page = request.args.get('per_page', 10, type=int)

            profesores = db.session.query(ProfesorModel.usuario, func.count(ClasesModel.id_clase)) \
                .outerjoin(ProfesorModel.clases) \
                .group_by(ProfesorModel.id_profesor) \
                .order_by(desc(func.count(ClasesModel.id_clase))) \
                .paginate(page=page, per_page=per_page, error_out=True)

            profesores_data = {
                "profesor": [
                    {
                        "profesor": profesor[0],
                        "cantidad_clases": profesor[1]
                    } for profesor in profesores.items
                ],
                "page": page,
                "pages": profesores.pages,
                "total": profesores.total
            }

            return jsonify(profesores_data)

        # devuelve los profesores con la cantidad de clases, vesion SQL(chequear)
        if request.args.get('alumnos'):
            db.execsql("""SELECT u.nombre, u.apellido, COUNT(a.id_alumno) AS cantidad_alumnos
                        FROM usuario u JOIN profesor p ON u.id_usuario = p.id_usuario
                        JOIN profesores_clases pc ON p.id_profesor = pc.id_profesor
                        JOIN clase c ON c.id_clase = pc.id_clase
                        JOIN planificacion pl ON pl.id_clase  = c.id_clase
                        JOIN alumnos_planificaciones ap ON pl.id_planificacion = ap.id_planificacion
                        JOIN alumno a ON a.id_alumno = ap.id_alumno
                        GROUP BY u.nombre
                        ORDER BY u.nombre DESC""")

        try:
            profesores = profesores.paginate(page=page, per_page=per_page, error_out=True)
        except Exception:
            return jsonify({"error": "Error inesperado"})

        return jsonify({"profesor": [profesor.to_json() for profesor in profesores],
                        "page": page,
                        "pages": profesores.pages,
                        "total": profesores.total
                        })

    @jwt_required()
    def post(self):
        try:
            data = request.get_json()
        except Exception:
            return "Error al pasar a JSON"
        clase = db.session.query(ClasesModel).filter(ClasesModel.tipo.like(data["clase"]["tipo"])).first()
        profesor = ProfesorModel.from_json(data["profesor"])
        clase.profesores_p.append(profesor)
        db.session.add(profesor)
        db.session.add(clase)
        db.session.commit()
        return profesor.to_json(), 201


class Profesor(Resource):

    @jwt_required(optional=True)
    def get(self, id):
        profesor = db.session.query(ProfesorModel).get_or_404(id)
        return profesor.to_json()

    @role_required(roles="admin")
    def put(self, id):
        profesor = db.session.query(ProfesorModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(profesor, key, value)
        db.session.add(profesor)
        db.session.commit()
        return profesor.to_json(), 201

    @role_required(roles="admin")
    def delete(self, id):
        profesor = db.session.query(ProfesorModel).get_or_404(id)
        db.session.delete(profesor)
        db.session.commit()
        return '', 204
