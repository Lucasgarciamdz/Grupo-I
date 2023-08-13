import unittest
import requests
import os
import faker


class TestSettings(unittest.TestCase):

    BASE_URL = f"http://localhost:{os.getenv('PORT', 5001)}"

    fake = faker.Faker()

    users = {
        "admin": {
            "nombre": fake.first_name(),
            "apellido": fake.last_name(),
            "direccion": fake.address(),
            "edad": fake.random_int(min=18, max=65),
            "telefono": fake.phone_number(),
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
            "telefono": fake.phone_number(),
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
            "telefono": fake.phone_number(),
            "dni": fake.random_int(min=10000000, max=99999999),
            "rol": "profesor",
            "sexo": fake.random_element(elements=("M", "F")),
            "email": "testing_profesor@gmail.com",
            "contrasena": "gYmbro543",
        }
    }

    sessions = {}

    def setUpClass(self):
        for rol, data in self.users.items():
            session = requests.Session()
            session.post(f"{self.BASE_URL}/auth/register", json=data)
            response = session.post(f"{self.BASE_URL}/auth/login", json=data)
            token = response.json()["access_token"]
            session.headers.update({"Authorization": f"Bearer {token}"})
            self.sessions[f"client_{rol}"] = session

    CLIENT_ADMIN = sessions["client_admin"]
    CLIENT_ALUMNO = sessions["client_alumno"]
    CLIENT_PROFESOR = sessions["client_profesor"]
