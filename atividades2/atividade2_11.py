def soma(a,b):
    return a+b
def subtracao(a,b):
    return a-b
def multiplicacao(a,b):
    return a*b
def divisao(a,b):
    return a/b



operacoes = { 'a':soma,'s':subtracao,'m':subtracao,'d':divisao}


print(operacoes['a'](int(input('Digite o primeiro numero')),int(input("digite o segundo numero"))))
