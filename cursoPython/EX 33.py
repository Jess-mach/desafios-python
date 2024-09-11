print('Escolha três números que vou anazilsar qual deles é o maior e qual menor.')
primeiro = int(input('Digite o primeiro numero:'))
segundo = int(input('Digite o segundo número:'))
terceiro = int(input('Digite o terceiro número:'))
#Verificando o menor valor
menor = primeiro
if segundo < primeiro and segundo < terceiro:
    menor = segundo
if terceiro < primeiro and terceiro < segundo:
    menor = terceiro
#Verificando o maior valor
maior = primeiro
if segundo > primeiro and segundo > terceiro:
    maior = segundo
if terceiro > primeiro and terceiro > segundo:
    maior = terceiro
print('{} é o menor número escolhido.'.format(menor))
print('{} é o maior número escolido.'.format(maior))
