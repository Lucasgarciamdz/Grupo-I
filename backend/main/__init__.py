from flask import Flask
from dotenv import load_dotenv
from flask_restful import Api

import main.resources as resources

api = Api()


# Vamos a crear un metodo que inicializara la app y todos los modulos
def create_app():
    # inicio Flask
    app = Flask(__name__)

    # variables de entono
    load_dotenv()

    # Aca iniciaremos los demas modulos de la app
    api.add_resource(resources.UsuariosResource, '/usuarios')
    api.add_resource(resources.UsuarioResource, '/usuario/<id>')
    api.add_resource(resources.AlumnosResource, '/alumnos')
    api.add_resource(resources.AlumnoResource, '/alumno/<id>')
    api.add_resource(resources.ProfesoresResource, '/profesores')
    api.add_resource(resources.ProfesorResource, '/profesor/<id>')
    api.add_resource(resources.ProfesorClasesResource, '/profesor_clases/<id>')
    api.add_resource(resources.ProfesoresClasesResource, '/profesores_clases')
    api.add_resource(resources.PagosResource, '/pagos')
    api.add_resource(resources.PagoResource, '/pago/<id>')
    api.add_resource(resources.PlanificacionesAlumnosResource, '/planificaciones_alumnos')
    api.add_resource(resources.PlanificacionAlumnoResource, '/planificacion_alumno/<id>')
    api.add_resource(resources.PlanificacionesProfesoresResource, '/planificaciones_profesores')
    api.add_resource(resources.PlanificacionProfesorResource, '/planificacion_profesor/<id>')
    api.add_resource(resources.LoginResource, '/login')
    api.init_app(app)
    # Por ultimo retornamos la aplicacion inicializada
    return app
