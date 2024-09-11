num1 = int(input('Digite um número :'))
num2 = int(input('Digite outro número:'))
print('Comparando os dois valores  podemos dizer que:')
if num1 > num2 :
    print('O valor {} é maior que o valor {}.'.format(num1,num2))
elif num2 > num1 :
    print('O valor {} é maior que o valor {}.'.format(num2,num1))
else:
    print('Não existe valor maior, os dois valores são iguais.')