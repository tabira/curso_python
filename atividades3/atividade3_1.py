from datetime import date


def diferenca_dias(data, hoje=None):
    if hoje is None:
        hoje = date.today()

    diferenca = hoje - data

    return diferenca.days


class Computador():

    def __init__(self, codigo: int, nome: str, aquisicao: date, vida: int, marca: object) -> object:
        self.codigo = codigo
        self.nome = nome
        self.aquisicao = aquisicao
        self.vida = vida
        self.marca = marca

    def alerta_manutencao(self, hoje=None):
        if hoje is None:
            hoje = date.today()
        diferenca = diferenca_dias(self.aquisicao, hoje)
        if self.vida < diferenca:
            print(f'Perido de manutenção expirado em {diferenca} dias')
        else:
            print(f'Ainda faltam {diferenca} dias para a manutencao')


class Marca():

    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome


dell = Marca(codigo=1, nome='dell')
hp = Marca(2, 'hp')

hp = Computador(
    codigo=1,
    nome='pavilion',
    aquisicao=date(2015, 1, 1),
    vida=365,
    marca=dell
)
vostro = Computador(
    codigo=2,
    nome='Vostror',
    aquisicao=date(2019, 1, 1),
    vida=365,
    marca=dell
)

hp.alerta_manutencao()
vostro.alerta_manutencao()
