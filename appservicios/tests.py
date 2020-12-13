from django.test import TestCase

from appservicios.models import Usuario

Class UsuarioModelTest(TestCase):
    @classmethod
    def test_usurio_max_length(self):
        usuario=Usuario.objects.get(id=1)
        max_length = Usuario._meta.get_field('usuario').max_length
        self.assertEquals(max_length,30)