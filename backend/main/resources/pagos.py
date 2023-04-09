from flask_restful import Resource
from .usuario import USUARIOS


PAGOS = {
    1: {'alumno': '1', 'monto': '1000', 'estado': 'Pendiente'},
    2: {'alumno': '2', 'monto': '1500', 'estado': 'Pagado'},
}


class Pago(Resource):
    def get(self, id):
        if int(id) in USUARIOS:
            return PAGOS[int(id)]
        return '', 404


class Pagos(Resource):
    def get(self):
        return PAGOS
