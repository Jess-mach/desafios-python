pag = float(input('Digite seu salário. R$:'))
novo = pag + (pag*15/100)
print('Seu salario atual é de R$:{:.2f} , e seu novo salário, com 15% de aumento, será de R$:{:.2f}'.format(pag,novo))
