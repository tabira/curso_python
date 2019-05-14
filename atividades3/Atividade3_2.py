class Pessoa():
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email


class Professor(Pessoa):
    def __init__(self, nome, email, categoria):
        super().__init__(nome, email)
        self.categoria = categoria


class Aluno(Pessoa)
    def __init__(self, nome, email, matricula):
        super().__init__(nome, email)
        self.matricula = matricula
       