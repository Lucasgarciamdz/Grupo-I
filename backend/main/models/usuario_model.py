from .. import db


class Usuario(db.Model):

    __tablename__ = "usuario"

    id_usuario = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(45), nullable=False)
    apellido = db.Column(db.String(45), nullable=False)
    direccion = db.Column(db.String(45), nullable=False)
    edad = db.Column(db.Integer(3), nullable=False)
    telefono = db.Column(db.Integer(15), nullable=False)
    dni = db.Column(db.Integer(8), nullable=False)
    rol = db.Column(db.String(45), nullable=False)
    sexo = db.Column(db.String(2), nullable=False)
    #id_login = db.Column(db.Integer, db.ForeignKey('Login.id_login'))

    def __repr__(self):
        return '<usuario: %r >' % (self.id_usuario)

    def to_json(self):
        usuario_json = {
            'id_usuario': str(self.id_usuario),
            'nombre': str(self.nombre),
            'apellido': str(self.apellido),
            'edad': str(self.edad),
            'dni': str(self.dni),
            'rol': str(self.rol),
            'sexo': str(self.sexo),
            # 'id_login': self.id_login

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
        # id_login = usuario_json.get('id_login')

        return Usuario(id_usuario=id_usuario,
                        nombre=nombre,
                        apellido=apellido,
                        direccion=direccion,
                        edad=edad,
                        telefono=telefono,
                        dni=dni,
                        rol=rol,
                        sexo=sexo,
                        # id_login=id_login
                        )
