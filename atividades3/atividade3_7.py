class Usuario():
    def __init__(self, nome, endereco, email, telefone, id):
        self.nome = nome
        self.endereco = endereco
        self.email = email
        self.telefone = telefone
        self.id = id


class Livro():
    def __init__(self, titulo, autor, publicacao, id, area, categoria):
        self.titulo = titulo
        self.autor = autor
        self.publicacao = publicacao
        self.id = id
        self.area = area
        self.categoria = categoria


class Avaliacao():
    avaliacoes =[]
    def __init__(self, usuario, livro, dt_avaliacao, nota, comentario):
        self.usuario = usuario
        self.livro = livro
        self.dt_avaliacao = dt_avaliacao
        self.nota = nota
        self.comentario = comentario
        self.avaliacoes.append(self)


arthur = Usuario('Artur de Camelote', 'Castelo de camelote', 'artur_rei@email.com', '5674-8901', 1.)

livro = Livro('Dive into Python 3', 'Mark Pilgrim', '06/11/2009', 42, 'Ciências Exatas', 'Programação de computadores')

avalicacao =Avaliacao(arthur, livro, '15/01/2015', 5, 'Excelente livro pois além de ser gratuito fornece ' +
          'armas poderosas para programadores e estudiosos')


print(avalicacao.avaliacoes)