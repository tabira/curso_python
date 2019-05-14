class Bairro():
    def __init__(self, nome):
        self.nome = nome


class Cidade():
    def __init__(self, nome, bairros):
        self.nome = nome
        self.bairros = bairros


class Estado():
    def __init__(self, nome, cidades):
        self.nome = nome
        self.cidades = cidades


class Pais():
    def __init__(self, nome, estados):
        self.nome = nome
        self.estados = estados


bairro = Bairro('centro')
