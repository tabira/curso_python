class Estabelecimento:
    def __init__(self, nome, endereco, classificacao):
        self.nome = nome
        self.endereco = endereco
        self.classificacao = classificacao


class Hotel(Estabelecimento):
    def __init__(self, nome, endereco, classificacao, rede, capacidade):
        self.rede = rede
        self.capacidade = capacidade
        super().__init__(nome, endereco, classificacao)


class Restaurante(Estabelecimento):
    def __init__(self, nome, endereco, classificacao,
                 especialidade, funcionamento):
        self.especialidade = especialidade
        self.funcionamento = funcionamento
        super().__init__(nome, endereco, classificacao)
