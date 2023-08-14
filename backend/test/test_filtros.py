from .test_settings import TestSettings
from models import profesor_model
from filtros import estado_filter


class TestFiltros(TestSettings):

    def register_profesor_filtrar_nombre(self):
        url = f"{self.BASE_URL}/auth/register"
        data = self.users["profesor"]

        for profesor in get("5", "profesores"):
            response = self.CLIENT_ADMIN.post(url, json=data)

        profesores = db.query(profesor_model.Profesor).all()

        self.assertEqual()
        profesores_filtrados = estado_filter(profesores, "activos")

        self.assertEqual(response.status_code, 200)
        self.assertNotIn("vencido", profesores_filtrados)
