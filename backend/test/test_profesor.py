from .test_settings import TestSettings


class TestProfesor(TestSettings):

    def primer_test(self):
        url = f"{self.BASE_URL}/profesor"
        data = self.users["profesor"]

        response = self.CLIENT_PROFESOR.post(url, json=data)
        self.assertEqual(response.status_code, 200)

    def test_jwt_alumno(self):
        url = f"{self.BASE_URL}/profesor/1"
        response = self.CLIENT_ALUMNO.get(url)

        self.assertEqual(response.status_code, 401)
