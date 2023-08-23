from factory import db
from werkzeug.security import generate_password_hash, check_password_hash
import json


class BaseModel(db.Model):
    __abstract__ = True

    @property
    def plain_contrasena(self):
        raise AttributeError('contrasena cant be read')

    @plain_contrasena.setter
    def plain_contrasena(self, contrasena):
        self.contrasena = generate_password_hash(contrasena)

    def validate_pass(self, contrasena):
        return check_password_hash(self.contrasena, contrasena)

    def to_json(self):
        db.session.refresh(self)
        data = self.__dict__.copy()
        del data['_sa_instance_state']
        del data['contrasena']
        return data

    @staticmethod
    def from_json(self, json_data):
        if isinstance(json_data, str):
            usuario_dict = json.loads(json_data)
        elif isinstance(json_data, dict):
            usuario_dict = json_data
        else:
            raise ValueError("Invalid JSON data")
        return self(**usuario_dict)
