import unittest
import requests
import os
import faker
from .client import SingletonClient


class TestSettings(unittest.TestCase):

    BASE_URL = f"http://localhost:{os.getenv('PORT', 5001)}"

    fake = faker.Faker()

    users = {
        "admin": {
            "nombre": fake.first_name(),
            "apellido": fake.last_name(),
            "direccion": fake.address(),
            "edad": fake.random_int(min=18, max=65),
            "telefono": 111113,
            "dni": fake.random_int(min=10000000, max=99999999),
            "rol": "admin",
            "sexo": fake.random_element(elements=("M", "F")),
            "email": "testing_admin@gmail.com",
            "contrasena": "123456",
        },
        "alumno": {
            "nombre": fake.first_name(),
            "apellido": fake.last_name(),
            "direccion": fake.address(),
            "edad": fake.random_int(min=18, max=65),
            "telefono": 111112,
            "dni": fake.random_int(min=10000000, max=99999999),
            "rol": "alumno",
            "sexo": fake.random_element(elements=("M", "F")),
            "email": "testing_alumno@gmail.com",
            "contrasena": "Fierro123",
        },
        "profesor": {
            "nombre": fake.first_name(),
            "apellido": fake.last_name(),
            "direccion": fake.address(),
            "edad": fake.random_int(min=18, max=65),
            "telefono": 111111,
            "dni": fake.random_int(min=10000000, max=99999999),
            "rol": "profesor",
            "sexo": fake.random_element(elements=("M", "F")),
            "email": "testing_profesor@gmail.com",
            "contrasena": "gYmbro543",
        }
    }

    sessions = {}

    @classmethod
    def setUpClass(cls):
        for rol, data in cls.users.items():
            session = requests.Session()
            response = session.post(f"{cls.BASE_URL}/auth/register", json=data)
            print(response.status_code)

            response = session.post(f"{cls.BASE_URL}/auth/login", json=data)
            token = response.json()["access_token"]
            session.headers.update({"Authorization": f"Bearer {token}"})
            cls.sessions[f"client_{rol}"] = SingletonClient(session)

        print(cls.sessions)
        cls.CLIENT_ADMIN = cls.sessions["client_admin"]
        cls.CLIENT_ALUMNO = cls.sessions["client_alumno"]
        cls.CLIENT_PROFESOR = cls.sessions["client_profesor"]
