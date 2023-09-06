from flask import Flask
from dotenv import load_dotenv
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from config import Config


db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()


def create_app():
    app = Flask("gym_api")
    load_dotenv()

    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

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
    from resources.readyz import Readyz as ReadyzResource

    api = Api(app)

    api.add_resource(UsuariosResource, '/usuarios')
    api.add_resource(UsuarioResource, '/usuario/<id_usuario>')
    api.add_resource(AlumnosResource, '/alumnos')
    api.add_resource(AlumnoResource, '/alumno/<id>')
    api.add_resource(ProfesoresResource, '/profesores')
    api.add_resource(ProfesorResource, '/profesor/<id>')
    api.add_resource(ClasesResource, '/clases')
    api.add_resource(ClaseResource, '/clase/<id>')
    api.add_resource(PlanificacionesResource, '/planificaciones')
    api.add_resource(PlanificacionResource, '/planificacion/<id>')
    api.add_resource(ReadyzResource, '/readyz')

    app.register_blueprint(rutas.auth)

    with app.app_context():
        db.create_all()

    return app
