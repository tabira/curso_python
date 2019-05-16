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
    cpf =  models.CharField(max_length=15,
                            default='',
                            verbose_name='CPF')

    class Meta:
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return 'Cliente - {} - {}'.format(self.id,self.nome)

    def registro_antigo(self):
        data_atual=timezone.now()
        diferenca =data_atual-self.registro
        return diferenca.days > 365
    registro_antigo.short_description = 'Cliente antigo?'
    registro_antigo.boolean = True
    registro_antigo.admin_order_field = 'registrado_em'


class Doador(models.Model):
    GENEROS = (('M', 'Masculino'), ('F', 'Feminino'))

    nome = models.CharField(max_length=200)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)
    email = models.CharField(max_length=200)
    registro = models.DateTimeField(auto_now_add=True)
    genero = models.CharField(max_length=2, choices=GENEROS)

    cpf = models.CharField(max_length=15,default='',
                            verbose_name = 'CPF')

    class Meta:
        verbose_name_plural='Doadores'


    def registro_antigo(self):
        data_atual=timezone.now()
        diferenca =data_atual-self.registro
        return diferenca.days > 365
    registro_antigo.short_description = 'Doador antigo?'
    registro_antigo.boolean = True
    registro_antigo.admin_order_field = 'registrado_em'




class Raca(models.Model):
    PORTES = (('P', 'Pequeno'), ('M', 'Médio'), ('G', 'Grande'))

    nome = models.CharField(max_length=200)
    porte = models.CharField(max_length=2, choices=PORTES)

    class Meta:
        verbose_name_plural='Raças'



class Animal(models.Model):
    nome = models.CharField(max_length=200)
    idade = models.IntegerField(default=0)
    especie = models.CharField(max_length=30)
    cor = models.CharField(max_length=20,default='')
    descricao = models.TextField()
    registro = models.DateTimeField(auto_now_add=True)
    raca = models.ForeignKey(Raca, on_delete=models.CASCADE)
    doador = models.ForeignKey(Doador, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural='Animais'



class Adocao(models.Model):
    registro = models.DateTimeField(default=timezone.now)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)




    class Meta:
        verbose_name_plural = 'Adoções'

    def __str__(self):
        return f'{self.cliente.nome} - {self.animal.nome}'
