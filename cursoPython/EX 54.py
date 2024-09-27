from datetime import date
atual = date.today().year
maior = 0
menor = 0
for ano in range(1,8):
    nasc = int(input(f'Digite o ano de nascimento da {ano}º pessoa:'))
    idade = atual - nasc
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print(f'Ao todo tivemos {maior} pessoas maior de idade.')
print(f'E também tivemos {menor} pessoas menores de idade.')