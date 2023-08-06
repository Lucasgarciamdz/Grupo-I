from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy


api = Api()

db = SQLAlchemy()

migrate = Migrate()

jwt = JWTManager()
