from django.db import models
from django.utils import timezone


class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    endereco = models.CharField(
        verbose_name='Endereço',
        max_length=200
    )
    telefone = models.CharField(max_length=20)
    email = models.EmailField(max_length=200)

    registrado_em = models.DateTimeField('data do registro')

    def telefone_numerico(self):
        teclado = str.maketrans('abcdefghijklmnopqrstuvwxyz',
                                '22233344455566677778889999')
        return self.telefone.translate(teclado)

    def __str__(self):
        return "{} - {}".format(self.id, self.nome)

    def registro_antigo(self):
        data_atual = timezone.now()
        diferenca = data_atual - self.registrado_em
        return diferenca.days > 365

    registro_antigo.short_description = 'Cliente antigo?'
    registro_antigo.boolean = True
    registro_antigo.admin_order_field = 'registrado_em'


class Reserva(models.Model):
    data_reserva = models.DateTimeField('data da reserva')
    data_evento = models.DateTimeField('data do evento')
    pessoas = models.IntegerField(default=0)
    cliente = models.ForeignKey(Cliente,
                                related_name='reservas',
                                on_delete=models.CASCADE)

    def __str__(self):
        return "{} - Cliente: {} ({}) - Pessoas {}".format(self.id,
                                                           self.cliente.nome,
                                                           self.data_evento.strftime("%d/%m/%Y - %H:%M:%S  "),
                                                           self.pessoas)
