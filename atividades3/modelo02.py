class Computador():

    def __init__(self, codigo: int, nome: str, aquisicao: str, vida: int, marca: object) -> object:
        self.codigo = codigo
        self.nome = nome
        self.aquisicao = aquisicao
        self.vida = vida
        self.marca = marca

    def alerta_manutencao(self):
        # todo: Calcular periodo de manutencao
        pass


class Marca():

    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome


dell = Marca(codigo=1, nome='dell')

computador = Computador(
    codigo=1,
    nome='pavilion',
    aquisicao='1/1/2019',
    vida=365,
    marca=dell
)

print(computador.marca.nome)

print(computador.marca is dell)

