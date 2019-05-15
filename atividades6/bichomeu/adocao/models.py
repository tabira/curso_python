from django.db import models
from django.utils import timezone


class Cliente(models.Model):
    GENEROS = (('M', 'Masculino'), ('F', 'Feminino'))

    nome = models.CharField(max_length=200)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)
    email = models.CharField(max_length=200)
    registro = models.DateTimeField(auto_now_add=True)
    genero = models.CharField(max_length=2, choices=GENEROS)
    cpf =  models.CharField(max_length=15,default='')

    def __str__(self):
        return 'Cliente - {} - {}'.format(self.id,self.nome)


class Doador(models.Model):
    GENEROS = (('M', 'Masculino'), ('F', 'Feminino'))

    nome = models.CharField(max_length=200)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)
    email = models.CharField(max_length=200)
    registro = models.DateTimeField(auto_now_add=True)
    genero = models.CharField(max_length=2, choices=GENEROS)

    cpf = models.CharField(max_length=15,default='')


class Raca(models.Model):
    PORTES = (('P', 'Pequeno'), ('M', 'Médio'), ('G', 'Grande'))

    nome = models.CharField(max_length=200)
    porte = models.CharField(max_length=2, choices=PORTES)


class Animal(models.Model):
    nome = models.CharField(max_length=200)
    idade = models.IntegerField(default=0)
    especie = models.CharField(max_length=30)
    cor = models.CharField(max_length=20,default='')
    descricao = models.TextField()
    registro = models.DateTimeField(auto_now_add=True)
    raca = models.ForeignKey(Raca, on_delete=models.CASCADE)
    doador = models.ForeignKey(Doador, on_delete=models.CASCADE)


class Adocao(models.Model):
    registro = models.DateTimeField(default=timezone.now)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
