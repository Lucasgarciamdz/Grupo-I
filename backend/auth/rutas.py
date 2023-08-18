from flask import request, Blueprint
from factory import db
from models.usuario_model import Usuario as UsuarioModel
from flask_jwt_extended import create_access_token
import logging


auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data:
        return 'Invalid request data', 400

    email = data.get('email')
    password = data.get('contrasena')

    if not email or not password:
        logging.error('Email and password are required')
        return 'Email and password are required', 400

    logging.info('Buscando en la base de datos el Email: %s', email)

    usuario = db.session.query(UsuarioModel).filter(UsuarioModel.email == email).scalar()

    logging.debug(usuario)
    if usuario.validate_pass(password):
        access_token = create_access_token(identity=usuario)
        data = {
            'id': str(usuario.id_usuario),
            'email': usuario.email,
            'access_token': access_token
        }

        return data, 200
    else:
        logging.error('Incorrect password')
        return 'Incorrect password', 401


@auth.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        if not data:
            return 'Invalid request data', 400

        print(data)
        usuario = UsuarioModel.from_json(data)
        exists = db.session.query(UsuarioModel).filter(UsuarioModel.email == usuario.email).scalar() is not None
        data = usuario.__dict__.copy()
        del data['_sa_instance_state']
        print(data)
        if exists:
            return 'Duplicated email', 409
        else:
            db.session.add(usuario)
            db.session.commit()
            # sendMail([usuario.email], "Bienvenido!", 'register', usuario=usuario)
            return usuario.to_json(), 201
    except Exception as e:
        db.session.rollback()
        return str(e), 500
    # data = request.get_json()
    # usuario = None
    # if "usuario" in data:
    #     usuario_data = data["usuario"]
    #     exists = db.session.query(UsuarioModel).filter(
    #         (UsuarioModel.email == usuario_data['email']) |
    #         (UsuarioModel.dni == usuario_data['dni']) |
    #         (UsuarioModel.telefono == usuario_data['telefono'])
    #     ).scalar() is not None
    #     if exists:
    #         return 'Duplicated email, dni, or telefono'
    #     else:
    #         usuario = UsuarioModel.from_json(usuario_data)
    # # profesor = ProfesorModel.from_json(data["profesor"])
    # # if "alumno" in data:
    # #     alumno = AlumnoModel.from_json(data["alumno"])
    # # response_profesor = None
    # # response_alumno = None
    # # usuario = UsuarioModel.from_json(data["usuario"])
    # # try:
    # #     db.session.add(usuario)
    # # except Exception:
    # #     db.session.rollback()
    # #     return "No se registro ningun usuario"

    # # if profesor:
    # #     profesor_dict = profesor.to_json()
    # #     last_usuario = db.session.query(UsuarioModel).order_by(UsuarioModel.id_usuario.desc()).first()
    # #     profesor_dict['id_usuario'] = last_usuario.id_usuario
    # #     try:
    # #         response_profesor = ProfesoresResource().post(data={"profesor": profesor_dict, "clase": data["clase"]})
    # #     except Exception:
    # #         db.session.rollback()
    # #         return "No hay clase" 

    # # elif alumno:
    # #     alumno_dict = alumno.to_json()
    # #     last_usuario = db.session.query(UsuarioModel).order_by(UsuarioModel.id_usuario.desc()).first()
    # #     alumno_dict['id_usuario'] = last_usuario.id_usuario
    # #     try:
    # #         response_alumno = AlumnosResource.post(data={"alumno": alumno_dict, "planificacion": data["planificacion"]})
    # #     except Exception:
    # #         db.session.rollback()
    # #         return "No hay planificacion"

    # db.session.commit()

    # # response_data = {}
    # # if usuario:
    # #     response_data['usuario'] = usuario.to_json()
    # # if response_profesor:
    # #     response_data['profesor'] = response_profesor
    # # if response_alumno:
    # #     response_data['alumno'] = response_alumno
    # # if response_data:
    # #     return response_data
    # # else:
    # #     return 'No data provided'
    # # except Exception:
    # #     db.session.rollback()
    # #     return "500"
