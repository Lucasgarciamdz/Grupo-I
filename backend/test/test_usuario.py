import unittest
import requests


class TestUsuario(unittest.TestCase):
    def test_usuario(self):
        url = "http://localhost:5001/auth/register"
        data = {
            "nombre": "Lucas",
            "apellido": "Garcia",
            "direccion": "123 Main St",
            "edad": 30,
            "telefono": 5551234,
            "dni": 12345678,
            "rol": "profesor",
            "sexo": "M",
            "email": "lu.garcia@gmail.com",
            "contrasena": "12354",
        }

        response = requests.post(url, json=data)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
