# import pandas as pd
# from sqlalchemy import create_engine
# import os
# from werkzeug.security import generate_password_hash, check_password_hash
# from main.models import UsuarioModel
# from ..main.models.alumno_model import Alumno
# from ..main.models.profesor_model import Profesor
# from ..main.models.clase_model import Clase
# from ..main.models.planificacion_model import Planificacion

# database_url = os.getenv('DATABASE_PATH')
# engine = create_engine(database_url)
# csv = ['usuarios.csv', 'alumnos.csv', 'profesores.csv', 'clases.csv', 
#        'planificaciones.csv', 'alumno_planificacione.csv', 'profesor_clase.csv']

# @property
# def plain_contrasena(self):
#     raise AttributeError('contrasena cant be read')

# @plain_contrasena.setter
# def plain_contrasena(self, contrasena):
#     return generate_password_hash(contrasena)

# def insert_usuario(path):

#     df = pd.read_csv(path)

#     for _, row in df.iterrows():
#         usuario = UsuarioModel(
#             nombre=row['nombre'],
#             apellido=row['apellido'],
#             direccion=row['direccion'],
#             edad=row['edad'],
#             telefono=row['telefono'],
#             dni=row['dni'],
#             rol=row['rol'],
#             sexo=row['sexo'],
#             email=row['email'],
#             plain_contrasena=plain_contrasena(row['contrasena']) 
#         )

#     with engine.begin() as conn:
#         conn.session.add(usuario)

# if __name__ == '__main__':
#     insert_usuario(path='/Users/francobertoldi/Desktop/Programacion 1/Grupo-I/backend/database/' + csv[0])
#     # insert_alumno(path=csv[1])
#     # insert_profesor(path=csv[2])
#     # insert_clase(path=csv[3])
#     # insert_planificacion(path=csv[4])
#     # insert_alumno_planificacion(path=csv[5])
#     # insert_profesor_clase(path=csv[6])
