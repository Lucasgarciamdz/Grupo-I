from flask_restful import Resource
from flask import request, jsonify
from main import db
from main.models import UsuarioModel
from sqlalchemy import func, desc, asc


class Usuarios(Resource):
    def get(self):
        usuarios = db.session.query(UsuarioModel)

        page = 1

        per_page = 10

        if request.args.get('page'):
            page = int(request.args.get('page'))
        if request.args.get('per_page'):
            per_page = int(request.args.get('per_page'))

        # devuelve los usuarios dado un determinado nombre
        if request.args.get('nombre'):
            usuarios = usuarios\
                        .filter(UsuarioModel.nombre.like('%' + request.args.get('nombre') + '%'))

        # devuelve todos los usuarios dado un determinado rol
        if request.args.get('rol'):
            usuarios = usuarios\
                        .filter(UsuarioModel.rol.like(request.args.get('rol')))

        # devuelve el usuario dado un determinado dni
        if request.args.get('dni'):
            usuarios = usuarios\
                        .filter(UsuarioModel.dni.like(request.args.get('dni')))

        # devuelve una lista ordenada de los usuarios por edad (NO ANDA O EL POSTMAN NO MUESTRA LAS COSAS ORDENADAS)
        if request.args.get('sort_by_edad'):
            usuarios = usuarios\
                        .order_by(desc(UsuarioModel.edad))

        try:
            usuarios = usuarios.paginate(page=page, per_page=per_page, error_out=True, )
        except:
            return jsonify({"error":"Error inesperado"})
        
        return jsonify({"usuario": [usuario.to_json() for usuario in usuarios],
                        "page": page,
                        "pages": usuarios.pages,
                        "total": usuarios.total
                        })

    def post(self):
        try:
            usuario = UsuarioModel.from_json(request.get_json())
        except:
            return "Error al pasara JSON"
        db.session.add(usuario)
        db.session.commit()
        return usuario.to_json(), 201


class Usuario(Resource):
    def get(self, id):
        usuario = db.session.query(UsuarioModel).get_or_404(id)
        return usuario.to_json()

    def put(self, id):
        usuario = db.session.query(UsuarioModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(usuario, key, value)
        db.session.add(usuario)
        db.session.commit()
        return usuario.to_json(), 201

    def delete(self, id):
        usuario = db.session.query(UsuarioModel).get_or_404(id)
        db.session.delete(usuario)
        db.session.commit()
        return '', 204
