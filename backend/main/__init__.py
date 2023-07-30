from flask import Flask
from dotenv import load_dotenv
from flask_restful import Api
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

api = Api()

db = SQLAlchemy()

migrate = Migrate()

jwt = JWTManager()


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

    import main.resources as resources

    api.add_resource(resources.UsuariosResource, '/usuarios')
    api.add_resource(resources.UsuarioResource, '/usuario/<id>')
    api.add_resource(resources.AlumnosResource, '/alumnos')
    api.add_resource(resources.AlumnoResource, '/alumno/<id>')
    api.add_resource(resources.ProfesoresResource, '/profesores')
    api.add_resource(resources.ProfesorResource, '/profesor/<id>')
    api.add_resource(resources.ClasesResource, '/clases')
    api.add_resource(resources.ClaseResource, '/clase/<id>')
    api.add_resource(resources.PlanificacionesResource, '/planificaciones')
    api.add_resource(resources.PlanificacionResource, '/planificacion/<id>')

    api.init_app(app)

    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = int(os.getenv('JWT_ACCESS_TOKEN_EXPIRES'))
    jwt.init_app(app)

    from main.auth import rutas
    app.register_blueprint(rutas.auth)

    with app.app_context():
        db.create_all()
    return app
