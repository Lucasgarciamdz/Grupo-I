from flask import request, Blueprint
from .. import db
from main.models import UsuarioModel, ProfesorModel, AlumnoModel, ClasesModel, PlanificacionModel
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


@auth.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        usuario = None
        if not data:
            return 'Invalid request data', 400
        if "usuario" in data:
            usuario = UsuarioModel.from_json(data["usuario"])
            exists = db.session.query(UsuarioModel).filter(UsuarioModel.email == usuario.email).scalar() is not None
            if exists:
                return 'Duplicated email', 409
            else:
                db.session.add(usuario)
        if "profesor" in data:
            profesor = ProfesorModel.from_json(data["profesor"])
            db.session.add(profesor)
        elif "alumno" in data:
            alumno = AlumnoModel.from_json(data["alumno"])
            db.session.add(alumno)
        if "clases" in data:
            clases = ClasesModel.from_json(data["clases"])
            db.session.add(clases)
        elif "planificacion" in data:
            planificacion = PlanificacionModel.from_json(data["planificacion"])
            db.session.add(planificacion)
        db.session.commit()
        if usuario:
            return usuario.to_json(), 201
        else:
            return 404
    except Exception as e:
        db.session.rollback()
        return str(e), 500