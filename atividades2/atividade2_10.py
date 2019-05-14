def cria_frase( palavras):
    return ' '.join(palavras)

palavra=True

frase=[]
while palavra:
    palavra= input('Digite algo, pressione <Enter para sair>' )
    frase.append(palavra)

print(cria_frase(frase))

