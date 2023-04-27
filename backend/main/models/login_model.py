from .. import db


class Login(db.Model):

    __tablename__ = "login"

    id_login = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(45), nullable=False)
    contrasena = db.Column(db.String(45), nullable=False)
    
    usuario = db.relationship('Usuario', uselist=False, back_populates='login', cascade="all, delete-orphan", single_parent=True)
    
    def __repr__(self):
        return '<login: %r >' % (self.id_login)

    def to_json(self):
        login_json = {
            'id': str(self.id_login),
            'email': self.email,
            'contrasena': self.contrasena, 
            }
        return login_json

    @staticmethod
    def from_json(login_json):
        id_login = login_json.get('id_login')
        email = login_json.get('email')
        contrasena = login_json.get('contrasena')
        return Login(id_login=id_login, 
                     email=email, 
                     contrasena=contrasena
                     )