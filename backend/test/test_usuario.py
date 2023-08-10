import unittest
import requests


class TestUsuario(unittest.TestCase):
    def test_usuario(self):
        url = "http://localhost:5001/auth/login"
        data = {
            "email": "lu.garcia@gmail.com",
            "contrasena": "12354",
        }

        response = requests.post(url, json=data)
        print(response)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
