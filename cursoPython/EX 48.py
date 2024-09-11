soma = 0
cont = 0
for c in range (1, 501, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print(f'A soma entre todos os {cont} multiplos de 3, que são impares entre 1 e 500 é {soma}')
