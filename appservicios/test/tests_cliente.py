from django.contrib.auth.models import User
from django.test import TestCase
from appservicios.models import Cliente

class ClienteModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Cliente.objects.create(nombre ="Diego", apellido="Paredes", edad=22, telefono="59599986", email="diego@meso.edu.gt")
        pass
    def test_nombre_max_length(self):
        cliente=Cliente.objects.get(id=1)
        max_length = cliente._meta.get_field('nombre').max_length
        self.assertEquals(max_length,25)

    def test_apellido_max_length(self):
        cliente=Cliente.objects.get(id=1)
        max_length = cliente._meta.get_field('apellido').max_length
        self.assertEquals(max_length,25)

    def test_email_max_length(self):
        cliente=Cliente.objects.get(id=1)
        max_length = cliente._meta.get_field('email').max_length
        self.assertEquals(max_length,25)

    def test_telefono_max_length(self):
        cliente=Cliente.objects.get(id=1)
        max_length = cliente._meta.get_field('telefono').max_length
        self.assertEquals(max_length,25)