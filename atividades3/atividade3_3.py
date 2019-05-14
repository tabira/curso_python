class Aluno():
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula


class Disciplina():
    def __init__(self, nome, carga_bimestral):
        self.nome = nome
        self.carga_bimestral = carga_bimestral


class Historico():
    def __init__(self, disciplina, aluno):
        self.disciplina = disciplina
        self.aluno = aluno
        self.registros = []

    def addRegistro(self,bimestre,faltas,nota):
        self.registros.append((bimestre,faltas,nota))


        

    def imprimirRelatorio(self):
        print(f'Matricula:{self.aluno.matricula}')
        print(f'Aluno: {self.aluno.nome}')
        print(f'Media: {self.}')


