from .. import db


class Usuario(db.Model):

    __tablename__ = "Usuario"

    id_usuario = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(45), nullable=False)
    apellido = db.Column(db.String(45), nullable=False)
    direccion = db.Column(db.String(45), nullable=False)
    edad = db.Column(db.Integer(3), nullable=False)
    telefono = db.Column(db.Integer(15), nullable=False)
    dni = db.Column(db.Integer(8), nullable=False)
    rol = db.Column(db.String(45), nullable=False)
    sexo = db.Column(db.String(2), nullable=False)
    id_login = db.Column(db.Integer, db.ForeignKey('Login.id_login'))

    def __repr__(self):
        return '<Usuario: %r >' % (self.id_usuario)

    def to_json(self):
        usuario_json = {
            'id': self.id_usuario,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'edad': self.edad,
            'dni': self.dni,
            'rol': self.rol,
            'sexo': self.sexo,
            'id_login': self.id_login

        }
        return usuario_json
    
# que carajo hace esto
    def to_json_short(self):
        animal_json = {
            'id': self.id_usuario,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'edad': self.edad,
            'dni': self.dni,
            'rol': self.rol,
            'sexo': self.sexo,
            'id_login': self.id_login

        }
        return animal_json

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
        id_login = usuario_json.get('id_login')

        return Usuario(id=id_usuario,
                        nombre=nombre,
                        apellido=apellido,
                        direccion=direccion,
                        edad=edad,
                        telefono=telefono,
                        dni=dni,
                        rol=rol,
                        sexo=sexo,
                        id_login=id_login
                        )
