import os
import logging


class Config:
    log_level = os.getenv('LOG_LEVEL', 'INFO')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES = int(os.getenv('JWT_ACCESS_TOKEN_EXPIRES'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    logging.basicConfig(level=logging.log_level)
