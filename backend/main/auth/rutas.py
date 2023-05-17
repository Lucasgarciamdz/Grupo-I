from flask import request, Blueprint
from .. import db
from main.models import UsuarioModel
from flask_jwt_extended import create_access_token

auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.route('/login', methods=['POST'])
def login():
    usuario = db.session.query(UsuarioModel).filter(UsuarioModel.email == request.get_json().get("email")).first_or_404()
    if usuario.validate_pass(request.get_json().get("contrasena")):
        access_token = create_access_token(identity=usuario)
        data = {
            'id': str(usuario.id_usuario),
            'email': usuario.email,
            'access_token': access_token
        }

        return data, 200
    else:
        return 'Contraseña incorrecta', 401


@auth.route('/register', methods=['POST'])
def register():
    usuario = UsuarioModel.from_json(request.get_json())
    exists = db.session.query(UsuarioModel).filter(UsuarioModel.email == usuario.email).scalar() is not None
    if exists:
        return 'Duplicated mail', 409
    else:
        try:
            db.session.add(usuario)
            db.session.commit()
        except Exception as error:
            db.session.rollback()
            return str(error), 409
        return usuario.to_json(), 201
