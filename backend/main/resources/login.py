from flask_restful import Resource
from flask import request
from .. import db
from main.models import LoginModel


class Login(Resource):
    def post(self):
        login = LoginModel.from_json(request.get_json())
        db.session.add(login)
        db.session.commit()
        return login.to_json(), 201

    def delete():
        login = db.session.query(LoginModel).get_or_404(id)
        db.session.delete(login)
        db.session.commit()
        return '', 204