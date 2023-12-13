from flask import request, Blueprint
from flask_jwt_extended import create_access_token

from main.mail.functions import sendMail
from main.models import UsuarioModel
from main.models.clase_model import Clase  # Importa el modelo clase_model.py
from main.models.planificacion_model import Planificacion  # Importa el modelo planificacion_model.py
from .. import db

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
        try:
            id_profesor = usuario.profesor.id_profesor
        except Exception:
            id_profesor = None

        try:
            id_alumno = usuario.alumno.id_alumno
        except Exception:
            id_alumno = None
        data = {
            'id_usuario': str(usuario.id_usuario),
            'id_profesor': str(id_profesor),
            'id_alumno': str(id_alumno),
            'email': usuario.email,
            'usuario': usuario.to_json()
        }
        access_token = create_access_token(identity=usuario, additional_claims=data)

        data['access_token'] = access_token

        return data, 200
    else:
        return 'Incorrect password', 401


@auth.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        # data.rol = ""
        if not data:
            return 'Invalid request data', 400

        usuario = UsuarioModel.from_json(data)
        exists = db.session.query(UsuarioModel).filter(UsuarioModel.email == usuario.email).scalar() is not None
        if exists:
            return 'Duplicated email', 409
        else:
            db.session.add(usuario)
            db.session.commit()
            sendMail([usuario.email], "Bienvenido!", 'register', usuario=usuario)
            return usuario.to_json(), 201
    except Exception as e:
        db.session.rollback()
        return str(e), 500


@auth.route('/clase/<int:id_clase>/planificaciones', methods=['GET'])
def obtener_planificaciones_de_clase(id_clase):
    try:
        # Consulta la base de datos para obtener las planificaciones de la clase específica
        clase = Clase.query.get(id_clase)
        if clase is None:
            return 'Clase no encontrada', 404

        planificaciones = Planificacion.query.filter_by(id_clase=id_clase).all()

        # Convierte las planificaciones en una lista de diccionarios
        planificaciones_data = [planificacion.to_json() for planificacion in planificaciones]

        return jsonify(planificaciones_data), 200

    except Exception as e:
        return str(e), 500
