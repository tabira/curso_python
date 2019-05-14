class Paralelepipedo:
    def __init__(self, largura, altura, profundidade):
        self.largura = largura
        self.profundidade = profundidade
        self.altura = altura

    @property
    def area(self):
        return 2 * (self.altura * self.largura) + 2 \
               * (self.largura * self.profundidade) + 2 * \
               (self.altura * self.profundidade)

    @property
    def volume(self):
        return self.largura * self.altura * self.profundidade

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, valor):
        if valor > 0:
            self._altura = valor
        else:
            raise ValueError()

    @property
    def largura(self):
        return self._largura

    @largura.setter
    def largura(self, valor):
        if valor > 0:
            self._largura = valor
        else:
            raise ValueError()

    @property
    def profundidade(self):
        return self._profundidade

    @profundidade.setter
    def profundidade(self, valor):
        if valor > 0:
            self._profundidade = valor
        else:
            raise ValueError()



bloco = Paralelepipedo(2,2,2)

print(bloco.area)
