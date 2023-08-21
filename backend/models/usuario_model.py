from werkzeug.security import generate_password_hash, check_password_hash
from factory import db
import json


class Usuario(db.Model):

    __tablename__ = "usuario"

    id_usuario = db.Column(db.Integer, primary_key=True)

    nombre = db.Column(db.String(45), nullable=False)
    apellido = db.Column(db.String(45), nullable=False)
    direccion = db.Column(db.String(256), nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    telefono = db.Column(db.Integer, nullable=False)
    dni = db.Column(db.Integer, nullable=False)
    rol = db.Column(db.String(45), nullable=False)
    sexo = db.Column(db.String(2), nullable=False)
    email = db.Column(db.String(45), nullable=False, unique=True)
    contrasena = db.Column(db.String(256), nullable=False)

    profesor = db.relationship('Profesor', back_populates='usuario', uselist=False, cascade="all, delete-orphan", single_parent=True)
    alumno = db.relationship('Alumno', back_populates='usuario', uselist=False, cascade="all, delete-orphan", single_parent=True)

    def __init__(self, nombre=None, apellido=None, direccion=None, edad=None, telefono=None, dni=None, rol=None, sexo=None, email=None, contrasena=None):
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.edad = edad
        self.telefono = telefono
        self.dni = dni
        self.rol = rol
        self.sexo = sexo
        self.email = email
        self.plain_contrasena = contrasena

    @property
    def plain_contrasena(self):
        raise AttributeError('contrasena cant be read')

    @plain_contrasena.setter
    def plain_contrasena(self, contrasena):
        self.contrasena = generate_password_hash(contrasena)

    def validate_pass(self, contrasena):
        return check_password_hash(self.contrasena, contrasena)

    def __repr__(self):
        return f'<usuario: {self.id_usuario} >'

    def to_json(self):
        db.session.refresh(self)
        data = self.__dict__.copy()
        del data['_sa_instance_state']
        return json.dumps(data)

    @staticmethod
    def from_json(json_data):
        if isinstance(json_data, str):
            usuario_dict = json.loads(json_data)
        elif isinstance(json_data, dict):
            usuario_dict = json_data
        else:
            raise ValueError("Invalid JSON data")
        return Usuario(**usuario_dict)
