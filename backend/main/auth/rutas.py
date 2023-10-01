from flask import request, Blueprint
from .. import db
from main.models import UsuarioModel
from flask_jwt_extended import create_access_token

from main.mail.functions import sendMail    

auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.route('/login', methods=['POST'])
def login():

    data = request.get_json()
    if not data:
        return 'Invalid request data', 400

    email = data.get('email')
    password = data.get('contrasena')

    if not email or not password:
        return 'Email and password are required', 400

    usuario = db.session.query(UsuarioModel).filter(UsuarioModel.email == email).first_or_404()
    if usuario.validate_pass(password):
        access_token = create_access_token(identity=usuario)
        data = {
            'id': str(usuario.id_usuario),
            'email': usuario.email,
            'access_token': access_token
        }

        return data, 200
    else:
        return 'Incorrect password', 401



@auth.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        if not data:
            return 'Invalid request data', 400

        usuario = UsuarioModel.from_json(data)
        exists = db.session.query(UsuarioModel).filter(UsuarioModel.email == usuario.email).scalar() is not None
        if exists:
            return 'Duplicated email', 409
        else:
            db.session.add(usuario)
            db.session.commit()
            sent = sendMail ([usuario.email], "Welcome!",'register', usuario=usuario)
            #return usuario.to_json(), 201
    except Exception as e:
        db.session.rollback()
        return str(e), 500
