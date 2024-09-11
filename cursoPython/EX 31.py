distancia = float(input('Digite a distancia de sua viagem:'))
#valor = distancia * 0.50 if distancia <=200 else distancia * 0.45
if distancia <= 200:
    valor = distancia * 0.50
else:
    valor = distancia * 0.45
print('O valor de sua passagem será de {} reais.'.format(valor))
