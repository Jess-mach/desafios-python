nota1 = float(input('Digite sua primeira nota:'))
nota2 = float(input('Digite sua segunda nota:'))
media = (nota1 + nota2) / 2
if media < 5:
    print(f'O aluno teve as notas {nota1} e {nota2} então sua media foi de {media}')
    print('O aluno está \033[31mREPROVADO\033[0m!')
elif 7 > media >= 5:
    print(f'O aluno teve as notas {nota1} e {nota2} então sua media foi de {media}')
    print('O aluno está em \033[31mRECUPERAÇÃO\033[0m!')
elif media >= 7:
    print(f'O aluno teve as notas {nota1} e {nota2} então sua media foi de {media}')
    print('O aluno está \033[31mAPROVADO\033[0m!\nParabens!!!')
