class Produto():
    def __init__(self, nome, imposto, custo):
        self.nome = nome
        self.imposto = imposto
        self.custo = custo

    def preco(self, quantidade=1):
        return (self.custo + (self.custo * self.imposto)) * quantidade


class Alimento(Produto):
    def __init__(self, nome, imposto, custo, validade):
        super().__init__(nome, imposto, custo)
        self.validade = validade


class Roupa(Produto):

    def __init__(self, nome, imposto, custo, tamanho):
        super().__init__(nome, imposto, custo)
        self.tamanho = tamanho


pasta_dente = Produto('pasta de dente', 0.7, 1.5)

print(pasta_dente.preco(10))

banana = Alimento('banana', 0.1, 0.5, 10)

print(banana.preco())

camisa = Roupa('Calvo', 0.45, 30.0, 'G')

print(camisa.preco())

from dataclasses import dataclass


@dataclass
class NovoProduto():
    nome: str
    preco: float


@dataclass
class FilhoProduto(NovoProduto):
    validade: int


filho= FilhoProduto()