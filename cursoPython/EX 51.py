termo = int(input('Digite o primeiro termo:'))
razao = int(input('Digite a  razão:'))
decimo = termo +(10-1) * razao
for c in range (termo, decimo, razao):
    print(c)
print('Acabou!')