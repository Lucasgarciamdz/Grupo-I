import unittest
import requests
from .settings import TestSettings
from .example_data import USUARIOS_RANDOM


class TestUsuario(TestSettings):

    def test_usuario_login(self):
        url = f"{self.BASE_URL}/auth/login"
        data = self.USUARIOS_RANDOM[0]

        response = self.CLIENT_ADMIN.post(url, json=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn("access_token", response.json())
        self.assertIn("email", response.json())
        self.assertIn("id", response.json())
        self.TEST_ID = response.json()["id"]

    def test_usuario_register(self):
        url = f"{self.BASE_URL}/auth/register"
        data = self.USUARIOS_RANDOM[0]

        response = self.CLIENT_ADMIN.post(url, json=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn("email", response.json())
        self.assertIn("id", response.json())

    def test_get_usuario_id(self):
        data = USUARIOS_RANDOM[0]
        register = self.CLIENT_ADMIN.post(f"{self.BASE_URL}/auth/register", data)
        self.assertEqual(register.status_code, 200)
        login_data = {"email": data["email"], "contrasena": data["contrasena"]}
        login = self.CLIENT_ADMIN.post(f"{self.BASE_URL}/auth/login", login_data)
        self.assertEqual(login.status_code, 200)
        user_id = login.json()["id"]
        url = f"{self.BASE_URL}/usuario/get/{user_id}"
        response = self.CLIENT_ADMIN.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.data["nombre"], response.json()["nombre"])
        self.assertEqual(self.data["apellido"], response.json()["apellido"])
        self.assertEqual(self.data["direccion"], response.json()["direccion"])
        self.assertEqual(self.data["edad"], response.json()["edad"])
        self.assertEqual(self.data["telefono"], response.json()["telefono"])
        self.assertEqual(self.data["dni"], response.json()["dni"])
        self.assertEqual(self.data["rol"], response.json()["rol"])
        self.assertEqual(self.data["sexo"], response.json()["sexo"])
        self.assertEqual(self.data["email"], response.json()["email"])

    def test_put_usuario_id(self):
        data = USUARIOS_RANDOM[0]
        register = self.CLIENT_ADMIN.post(f"{self.BASE_URL}/auth/register", data)
        self.assertEqual(register.status_code, 200)
        login_data = {"email": data["email"], "contrasena": data["contrasena"]}
        login = self.CLIENT_ADMIN.post(f"{self.BASE_URL}/auth/login", login_data)
        self.assertEqual(login.status_code, 200)
        user_id = login.json()["id"]
        url = f"{self.BASE_URL}/usuario/put/{user_id}"
        response = self.CLIENT_ADMIN.get(url)
        url = f"{self.BASE_URL}/usuario/get/{user_id}"
        response = self.CLIENT_ADMIN.get(url)

if __name__ == '__main__':
    unittest.main()
