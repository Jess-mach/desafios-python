nun = 0
total = 0
n = 0
while nun != 999:
    nun = int(input('Digite um número ou 999 para sair:'))
    if nun != 999:
        total = total + nun
        n += 1
print(f'Foram {n} números e sua soma foi: {total}')
print('FIM')
