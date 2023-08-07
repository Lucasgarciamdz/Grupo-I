from werkzeug.security import generate_password_hash, check_password_hash
from factory import db


class Usuario(db.Model):

    __tablename__ = "usuario"

    id_usuario = db.Column(db.Integer, primary_key=True)

    nombre = db.Column(db.String(45), nullable=False)
    apellido = db.Column(db.String(45), nullable=False)
    direccion = db.Column(db.String(45), nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    telefono = db.Column(db.Integer, nullable=False)
    dni = db.Column(db.Integer, nullable=False)
    rol = db.Column(db.String(45), nullable=False)
    sexo = db.Column(db.String(2), nullable=False)
    email = db.Column(db.String(45), nullable=False, unique=True)
    contrasena = db.Column(db.String(45), nullable=False)

    # login = db.relationship('Login', back_populates='usuario', cascade="all, delete-orphan", uselist=False, single_parent=True)
    profesor = db.relationship('Profesor', back_populates='usuario', uselist=False, cascade="all, delete-orphan", single_parent=True)
    alumno = db.relationship('Alumno', back_populates='usuario', uselist=False, cascade="all, delete-orphan", single_parent=True)

    @property
    def plain_contrasena(self):
        raise AttributeError('contrasena cant be read')

    @plain_contrasena.setter
    def plain_contrasena(self, contrasena):
        self.contrasena = generate_password_hash(contrasena)

    def validate_pass(self, contrasena):
        return check_password_hash(self.contrasena, contrasena)

    def __repr__(self):
        return '<usuario: %r >' % (self.id_usuario)

    def to_json(self):
        usuario_json = {
            'id_usuario': self.id_usuario,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'direccion': self.direccion,
            'edad': self.edad,
            'telefono': self.telefono,
            'dni': self.dni,
            'rol': self.rol,
            'sexo': self.sexo,
            'email': self.email,
        }
        return usuario_json

    @staticmethod
    def from_json(usuario_json):
        id_usuario = usuario_json.get('id_usuario')
        nombre = usuario_json.get('nombre')
        apellido = usuario_json.get('apellido')
        direccion = usuario_json.get('direccion')
        edad = usuario_json.get('edad')
        telefono = usuario_json.get('telefono')
        dni = usuario_json.get('dni')
        rol = usuario_json.get('rol')
        sexo = usuario_json.get('sexo')
        email = usuario_json.get('email')
        contrasena = usuario_json.get('contrasena')

        return Usuario(id_usuario=id_usuario,
                       nombre=nombre,
                       apellido=apellido,
                       direccion=direccion,
                       edad=edad,
                       telefono=telefono,
                       dni=dni,
                       rol=rol,
                       sexo=sexo,
                       email=email,
                       plain_contrasena=contrasena,
                       )
