'''sexo = str(input('Digite seu genero [M/F]:')).strip().upper()[0]

while sexo != 'M' and sexo != 'F':
    print('Opção invalida digite novamente.')
    sexo = str(input('Digite seu genero [M/F]:')).strip().upper()[0]

if sexo == 'M':
    print('Você digitou M.')
if sexo == 'F':
    print('Você digitou F.')

print('Fim')'''

sexo = str(input('Informe seu sexo: [M\F]'))
while sexo not in 'MmFf':
  sexo = str(input('Dados inválidos. Por favor, informe seu sexo:')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso')
