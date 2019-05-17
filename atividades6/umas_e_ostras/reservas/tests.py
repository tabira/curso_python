from django.test import TestCase
from django.utils import timezone
from .models import Cliente


# Create your tests here.

class ClienteMethodTeste(TestCase):

    def teste_cliente_telefone_numero(self):
        cliente = Cliente(
            nome='Dr.',
            endereco='Hill Valley',
            telefone='de-lore-an12',
            email='doc@future.com',
            registrado_em=timezone.now()
        )
        self.assertEqual(
            cliente.telefone_numerico(), '33-5673-2612'
        )
