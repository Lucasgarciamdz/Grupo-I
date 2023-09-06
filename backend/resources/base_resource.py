
from flask import request
from flask_restful import Resource
from factory import db
from auth.decoradores import role_required
from flask_jwt_extended import jwt_required


class BaseResource(Resource):
    model_class = None

    @jwt_required(optional=True)
    def get(self, id):
        obj = db.session.query(self.model_class).get_or_404(id)
        return obj.to_json()

    @role_required(roles="admin")
    def put(self, id):
        obj = db.session.query(self.model_class).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(obj, key, value)
        db.session.add(obj)
        db.session.commit()
        return obj.to_json(), 201

    @role_required(roles="admin")
    def delete(self, id):
        obj = db.session.query(self.model_class).get_or_404(id)
        db.session.delete(obj)
        db.session.commit()
        return '', 204
