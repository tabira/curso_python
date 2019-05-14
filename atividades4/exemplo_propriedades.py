class Computador:
    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome

    @property
    def codigo(self):
        return self._codigo+20

    @codigo.setter
    def codigo(self, valor):
        if valor > 0:
            self._codigo = valor
        else:
            raise ValueError('Deve ser mairo que zero')



c = Computador(1, 'dell')

print(c.codigo)
print(c.codigo)
