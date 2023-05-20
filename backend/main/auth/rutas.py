from flask import request, Blueprint
from .. import db
from main.models import UsuarioModel, ProfesorModel, AlumnoModel, ClasesModel, PlanificacionModel
from main.resources import ProfesorResource, AlumnoResource, ClasesResource, PlanificacionResource, UsuarioResource
from flask_jwt_extended import create_access_token

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


def add_objects_to_session(data):
    usuario = None
    profesor = None
    alumno = None
    clase = None
    planificacion = None
    if "usuario" in data:
        usuario_data = data["usuario"]
        exists = db.session.query(UsuarioModel).filter(
            (UsuarioModel.email == usuario_data['email']) |
            (UsuarioModel.dni == usuario_data['dni']) |
            (UsuarioModel.telefono == usuario_data['telefono'])
        ).scalar() is not None
        if exists:
            return 'Duplicated email, dni, or telefono', 409
        else:
            usuario = UsuarioModel.from_json(usuario_data)
    if "profesor" in data:
        profesor = ProfesorModel.from_json(data["profesor"])
    elif "alumno" in data:
        alumno = AlumnoModel.from_json(data["alumno"])
    if "clase" in data:
        clase = ClasesModel.from_json(data["clase"])
    elif "planificacion" in data:
        planificacion = PlanificacionModel.from_json(data["planificacion"])
    return usuario, profesor, alumno, clase, planificacion


@auth.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        usuario, profesor, alumno, clase, planificacion = add_objects_to_session(data)
        if clase:
            clase_resource = ClasesResource()
            response = clase_resource.post(data=clase.to_json())
            if response.status_code != 201:
                db.session.rollback()
                return response.json(), response.status_code
        if profesor:
            profesor_resource = ProfesorResource()
            if "clase" in data:
                response = profesor_resource.post(data={"profesor": profesor.to_json(), "clase": data["clase"]})
            else:
                response = profesor_resource.post(data={"profesor": profesor.to_json()})
            if response.status_code != 201:
                db.session.rollback()
                return response.json(), response.status_code
        db.session.commit()
        response_data = {}
        if usuario:
            response_data['usuario'] = usuario.to_json()
        if profesor:
            response_data['profesor'] = profesor.to_json()
        if alumno:
            response_data['alumno'] = alumno.to_json()
        if clase:
            response_data['clase'] = clase.to_json()
        if planificacion:
            response_data['planificacion'] = planificacion.to_json()
        if response_data:
            return response_data, 201
        else:
            return 'No data provided', 400
    except Exception as e:
        db.session.rollback()
        return str(e), 500
