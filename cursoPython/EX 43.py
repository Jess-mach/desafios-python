peso = float(input('Digite seu peso:'))
altura = float(input('Digite sua altura:'))
print ('Vamos calcular seu IMC.')
imc =  peso / (altura ** 2)
if imc < 18.5:
    print (f'Seu IMC deu {imc:.2f}.Você está Abaixo do peso.')
elif 18.5 <= imc < 25:
    print(f'Seu IMC deu {imc:.2f}.Você está em seu peso ideal.')
elif 25 <= imc < 30:
    print(f'Seu IMC deu {imc:.2f}.Você está com Sobrepeso.')
elif 30 <= imc < 40:
    print(f'Seu IMC deu {imc:.2f}.Você está com Obesidade.')
else:
    print(f'Seu IMC deu {imc:.2f}. Você está com OBESIDADE MORBIDA.')
