from flask_restful import Resource
from flask import Response


class Readyz(Resource):
    def get(self):
        return Response("OK", status=200, mimetype='application/json')
