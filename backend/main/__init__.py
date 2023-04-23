from flask import Flask
from dotenv import load_dotenv
from flask_restful import Api
import os
from flask_sqlalchemy import SQLAlchemy

api = Api()

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    load_dotenv()

    if not os.path.exists(os.getenv('DATABASE_PATH')+os.getenv('DATABASE_NAME')):
        os.mknod(os.getenv('DATABASE_PATH')+os.getenv('DATABASE_NAME'))

    # with open(os.path.join(os.getenv('DATABASE_PATH'), os.getenv('DATABASE_NAME')), 'w'):
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////'+os.getenv('DATABASE_PATH')+os.getenv('DATABASE_NAME')
    db.init_app(app)

    import main.resources as resources

    api.add_resource(resources.UsuariosResource, '/usuarios')
    api.add_resource(resources.UsuarioResource, '/usuario/<id>')
    api.add_resource(resources.AlumnosResource, '/alumnos')
    api.add_resource(resources.AlumnoResource, '/alumno/<id>')
    api.add_resource(resources.ProfesoresResource, '/profesores')
    api.add_resource(resources.ProfesorResource, '/profesor/<id>')
    api.add_resource(resources.ClasesResource, '/profesor/<id>')
    api.add_resource(resources.ClaseResource, '/profesor/<id>')
    api.add_resource(resources.PlanificacionesResource, '/profesor/<id>')
    api.add_resource(resources.PlanificacionResource, '/profesor/<id>')
    api.add_resource(resources.LoginResource, '/login')
    # api.add_resource(resources.ProfesorClasesResource, '/profesor_clases/<id>')
    # api.add_resource(resources.ProfesoresClasesResource, '/profesores_clases')
    # api.add_resource(resources.PagosResource, '/pagos')
    # api.add_resource(resources.PagoResource, '/pago/<id>')
    # api.add_resource(resources.PlanificacionesAlumnosResource, '/planificaciones_alumnos')
    # api.add_resource(resources.PlanificacionAlumnoResource, '/planificacion_alumno/<id>')
    # api.add_resource(resources.PlanificacionesProfesoresResource, '/planificaciones_profesores')
    # api.add_resource(resources.PlanificacionProfesorResource, '/planificacion_profesor/<id>')
    api.init_app(app)
    # Por ultimo retornamos la aplicacion inicializada
    return app
