nome = str(input('Digite seu nome completo:')).strip()
print('Analisando seu nome...')
print('Nome em letras maiúsculas: {}'.format(nome.upper()))
print('Nome em letras minúsculas: {}'.format(nome.lower()))
print('Seu nome contém {} letras'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome contém {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras.'.format(separa[0], len(separa[0])))



