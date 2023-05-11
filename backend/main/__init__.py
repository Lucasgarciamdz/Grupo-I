from flask import Flask
from dotenv import load_dotenv
from flask_restful import Api
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

api = Api()

db = SQLAlchemy()

migrate = Migrate()
<<<<<<< HEAD

=======
>>>>>>> develop

def create_app():
    app = Flask(__name__)
    load_dotenv()

    database_path = os.getenv('DATABASE_PATH')
    database_name = os.getenv('DATABASE_NAME')
    full_path = os.path.join(database_path, database_name)

    if not os.path.exists(database_path):
        os.makedirs(database_path)

    if not os.path.exists(full_path):
        os.mknod(full_path)

    # with open(os.path.join(os.getenv('DATABASE_PATH'), os.getenv('DATABASE_NAME')), 'w'):
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////'+os.getenv('DATABASE_PATH')+os.getenv('DATABASE_NAME')
    db.init_app(app)
<<<<<<< HEAD
    migrate.init_app(app, db)
=======
    migrate.init_app(app,db)
>>>>>>> develop

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
    
    with app.app_context():
        db.create_all()
    api.init_app(app)
    # Por ultimo retornamos la aplicacion inicializada
    return app
