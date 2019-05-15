from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(max_length=200)
    registrado_em = models.DateTimeField('data do registro')


class Reserva(models.Model):
    data_reserva = models.DateTimeField('data da reserva')
    data_evento = models.DateTimeField('data do evento')
    pessoas = models.IntegerField(default=0)
    cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)
