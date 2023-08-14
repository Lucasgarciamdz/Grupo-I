import unittest
import requests
from .test_settings import TestSettings


class TestUsuario(TestSettings):
    def test_usuario(self):
        url = f"{self.BASE_URL}/auth/login"
        data = self.users["admin"]

        response = requests.post(url, json=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn("access_token", response.json())
        self.assertIn("email", response.json())
        self.assertIn("id", response.json())


if __name__ == '__main__':
    unittest.main()
