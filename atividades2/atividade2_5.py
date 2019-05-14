alunos = {'Carlos Miyamoto', 'Francisco Bento', 'Richard Meyer', 'Milla Vodello', 'Leona Heidern'}

 # Alunos aprovados em matemática.
matematica = {'Richard Meyer', 'Milla Vodello', 'Leona Heidern'}

# Alunos aprovados em física.
fisica = {'Carlos Miyamoto', 'Milla Vodello', 'Leona Heidern'}

aprovados = matematica & fisica
print (aprovados)

aprovados_em_algo = matematica | fisica
print (aprovados_em_algo)

aprovados_so_matematica = matematica-fisica
print (aprovados_so_matematica)

aprovados_so_fisica = matematica
