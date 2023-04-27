from .. import db


class Usuario(db.Model):

    __tablename__ = "usuario"

    id_usuario = db.Column(db.Integer, primary_key=True)
    id_login = db.Column(db.Integer, db.ForeignKey('login.id_login'))

    nombre = db.Column(db.String(45), nullable=False)
    apellido = db.Column(db.String(45), nullable=False)
    direccion = db.Column(db.String(45), nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    telefono = db.Column(db.Integer, nullable=False)
    dni = db.Column(db.Integer, nullable=False)
    rol = db.Column(db.String(45), nullable=False)
    sexo = db.Column(db.String(2), nullable=False)
    
    login = db.relationship('Login', back_populate='usuario', cascade="all, delete-orphan", use_list=False, single_parent=True)
    profesor = db.relationship('Profesor', back_populates='usuario', use_list=False, cascade="all, delete-orphan", single_parent=True)
    alumno = db.relationship('Alumno', back_populates='usuario', use_list=False, cascade="all, delete-orphan", single_parent=True)

    def __repr__(self):
        return '<usuario: %r >' % (self.id_usuario)

    def to_json(self):
        usuario_json = {
            'id': str(self.id_usuario),
            'id_login': self.id_login,
            'nombre': str(self.nombre),
            'apellido': str(self.apellido),
            'direccion': self.direccion,
            'edad': str(self.edad),
            'telefono': str(self.telefono),
            'dni': str(self.dni),
            'rol': str(self.rol),
            'sexo': str(self.sexo),

        }
        return usuario_json

    @staticmethod
    def from_json(usuario_json):
        id_usuario = usuario_json.get('id_usuario')
        id_login = usuario_json.get('id_login')
        nombre = usuario_json.get('nombre')
        apellido = usuario_json.get('apellido')
        direccion = usuario_json.get('direccion')
        edad = usuario_json.get('edad')
        telefono = usuario_json.get('telefono')
        dni = usuario_json.get('dni')
        rol = usuario_json.get('rol')
        sexo = usuario_json.get('sexo')

        return Usuario(id_usuario=id_usuario,
                       id_login=id_login,
                       nombre=nombre,
                       apellido=apellido,
                       direccion=direccion,
                       edad=edad,
                       telefono=telefono,
                       dni=dni,
                       rol=rol,
                       sexo=sexo,
                       )
