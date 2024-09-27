resp = 'S'
quant = soma = media = menor = maior = 0
while resp in 'S':
    nun = int(input('Digite um número:'))
    quant += 1
    soma += nun
    if quant == 1:
        maior = menor = nun
    else:
        if nun > maior:
            maior = nun
        if nun < menor:
            menor = nun
    resp= str(input('Quer continuar? [S/N]')).upper()
media = soma / quant
print(f'Você digitou {quant} números e a média entre eles foi {media}')
print(f'O maior número foi {maior} e o menor {menor}')
