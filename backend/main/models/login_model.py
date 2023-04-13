from .. import db


class Login(db.Model):

    __tablename__ = "Login"
    
    id_login = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(45), nullable=False)
    contraseña = db.Column(db.String(45), nullable=False)

    def __repr__(self):
        return '<Alumno: %r >' % (self.id_alumno)

    def to_json(self):
        login_json = {
            'id': self.id_login,
            'email': self.email,
            'contraseña': self.contraseña,

        }
        return login_json
    
# que carajo hace esto
    def to_json_short(self):
        animal_json = {
            'id': self.id_login,
            'email': self.email,
            'contraseña': self.contraseña,

        }
        return animal_json

    @staticmethod
    def from_json(login_json):
        id_login = login_json.get('id_login')
        email = login_json.get('email')
        contraseña = login_json.get('contraseña')
        return Login(id=id_login,
                        email=email,
                        contraseña=contraseña
                        )
