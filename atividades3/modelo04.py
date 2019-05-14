class Aluno():

    def __init__(self, matricula, nome):
        self.nome = nome
        self.matricula = matricula
        self.livros = []

    def empresta_livro(self, livro):
        self.livros.append(livro)


rodrigo = Aluno(1, 'Rodrigo')

rodrigo.empresta_livro('Python Fluente')

print(rodrigo.livros)

print(Aluno.empresta_livro)

# comment: executa o metodo na definicao da classe passando o objeto
Aluno.empresta_livro(rodrigo, 'Node.js')

print(rodrigo.livros)
