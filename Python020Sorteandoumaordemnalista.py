from random import shuffle
a = input('Primeiro aluno: ')
b = input('Segundo aluno: ')
c = input('Terceiro aluno: ')
d = input ('Quarto aluno: ')
alunos = [a,b,c,d]
shuffle(alunos)
print(f'A ordem de apresentação será: \n{alunos}.')
