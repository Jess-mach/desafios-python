velocidade = float(input('Digite a velocidade do seu carro:'))
if velocidade > 80:
    print('Você será multado por ultrapassar a velocidade permitida de 80km/h.')
    multa = (velocidade - 80) * 7
    print(' Sua multa será de {:.2f} reais.'.format(multa))
else:
    print('Parabens, você está dirigindo dentro da velocidade permitida! Boa viagem!')
