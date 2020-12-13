from django.contrib.auth.models import User
from django.test import TestCase
from appservicios.models import Usuario, Cliente

class UsuarioModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Usuario.objects.create(usuario = 'daga', password = '1234')
        pass

    def test_usurio_max_length(self):
        usuario=Usuario.objects.get(id=1)
        max_length = usuario._meta.get_field('usuario').max_length
        self.assertEquals(max_length,30)

    def test_password_max_length(self):
        usuario=Usuario.objects.get(id=1)
        max_length = usuario._meta.get_field('password').max_length
        self.assertEquals(max_length,30)