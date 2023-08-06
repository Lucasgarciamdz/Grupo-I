from flask import Flask
from dotenv import load_dotenv
import os
from auth import rutas
from resources.usuario import Usuarios as UsuariosResource
from resources.usuario import Usuario as UsuarioResource
from resources.alumno import Alumnos as AlumnosResource
from resources.alumno import Alumno as AlumnoResource
from resources.profesor import Profesores as ProfesoresResource
from resources.profesor import Profesor as ProfesorResource
from resources.clases import Clase as ClaseResource
from resources.clases import Clases as ClasesResource
from resources.planificaciones import Planificaciones as PlanificacionesResource
from resources.planificaciones import Planificacion as PlanificacionResource
from app import db, migrate, jwt, api


def create_app():
    app = Flask(__name__)
    load_dotenv()

    database_path = os.getenv('DATABASE_PATH')
    database_name = os.getenv('DATABASE_NAME')
    full_path = os.path.join(database_path, database_name)

    if not os.path.isdir(database_path):
        os.makedirs(database_path)

    if not os.path.exists(full_path):
        open(full_path, 'a').close()

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")
    db.init_app(app)
    migrate.init_app(app, db)

    api.add_resource(UsuariosResource, '/usuarios')
    api.add_resource(UsuarioResource, '/usuario/<id>')
    api.add_resource(AlumnosResource, '/alumnos')
    api.add_resource(AlumnoResource, '/alumno/<id>')
    api.add_resource(ProfesoresResource, '/profesores')
    api.add_resource(ProfesorResource, '/profesor/<id>')
    api.add_resource(ClasesResource, '/clases')
    api.add_resource(ClaseResource, '/clase/<id>')
    api.add_resource(PlanificacionesResource, '/planificaciones')
    api.add_resource(PlanificacionResource, '/planificacion/<id>')

    api.init_app(app)

    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = int(os.getenv('JWT_ACCESS_TOKEN_EXPIRES'))
    jwt.init_app(app)

    app.register_blueprint(rutas.auth)

    with app.app_context():
        db.create_all()
    return app


if __name__ == '__main__':
    db.create_all()
    create_app().run(debug=True, port=os.getenv('PORT'))
