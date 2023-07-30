from flask import request, Blueprint
from .. import db
from main.models import UsuarioModel, ProfesorModel, AlumnoModel, ClasesModel, PlanificacionModel
from main.resources import ProfesoresResource, AlumnosResource
from flask_jwt_extended import create_access_token
import pdb

auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.route('/login', methods=['POST'])
def login():
    try:
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
    except Exception as e:
        return str(e), 500


@auth.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    usuario = None
    if "usuario" in data:
        usuario_data = data["usuario"]
        exists = db.session.query(UsuarioModel).filter(
            (UsuarioModel.email == usuario_data['email']) |
            (UsuarioModel.dni == usuario_data['dni']) |
            (UsuarioModel.telefono == usuario_data['telefono'])
        ).scalar() is not None
        if exists:
            return 'Duplicated email, dni, or telefono'
        else:
            usuario = UsuarioModel.from_json(usuario_data)
    # profesor = ProfesorModel.from_json(data["profesor"])
    # if "alumno" in data:
    #     alumno = AlumnoModel.from_json(data["alumno"])
    # response_profesor = None
    # response_alumno = None
    # usuario = UsuarioModel.from_json(data["usuario"])
    # try:
    #     db.session.add(usuario)
    # except Exception:
    #     db.session.rollback()
    #     return "No se registro ningun usuario"

    # if profesor:
    #     profesor_dict = profesor.to_json()
    #     last_usuario = db.session.query(UsuarioModel).order_by(UsuarioModel.id_usuario.desc()).first()
    #     profesor_dict['id_usuario'] = last_usuario.id_usuario
    #     try:
    #         response_profesor = ProfesoresResource().post(data={"profesor": profesor_dict, "clase": data["clase"]})
    #     except Exception:
    #         db.session.rollback()
    #         return "No hay clase" 

    # elif alumno:
    #     alumno_dict = alumno.to_json()
    #     last_usuario = db.session.query(UsuarioModel).order_by(UsuarioModel.id_usuario.desc()).first()
    #     alumno_dict['id_usuario'] = last_usuario.id_usuario
    #     try:
    #         response_alumno = AlumnosResource.post(data={"alumno": alumno_dict, "planificacion": data["planificacion"]})
    #     except Exception:
    #         db.session.rollback()
    #         return "No hay planificacion"

    db.session.commit()

    # response_data = {}
    # if usuario:
    #     response_data['usuario'] = usuario.to_json()
    # if response_profesor:
    #     response_data['profesor'] = response_profesor
    # if response_alumno:
    #     response_data['alumno'] = response_alumno
    # if response_data:
    #     return response_data
    # else:
    #     return 'No data provided'
    # except Exception:
    #     db.session.rollback()
    #     return "500"
