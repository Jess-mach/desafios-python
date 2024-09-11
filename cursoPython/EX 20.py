from random import shuffles
a1 = input('Primeiro aluno:')
a2 = input('Segundo aluno:')
a3 = input('Terceiro aluno:')
a4 = input('Quarto aluno:')
lista = [a1, a2, a3, a4]
shuffles(lista)
print('A ordem dos alunos para apresentação é:', lista)
