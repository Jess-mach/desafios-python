casa = float(input('Qual será o valor da casa a comprar?'))
salario = float(input('Qual é o valor do seu seu sálario?'))
ano = float(input('Em quantos anos  pretende pagar o emprestimo?'))
#tranformado ano em parcelas
parcela = casa /(ano * 12)
#verificando salario
if parcela <= salario * 0.30 :
#ou  parcela <= salario * 30/100[ou ] criar uma nova variavel ex : minimo = salario * 30/100
    print ('O valor da casa é de {}. E o Valor mensal a pagar é R$:{:.1f}'.format(casa,parcela))
else:
    print('Infelismente seu empréstimo será negado, visto que a parcela a pagar será maior que 30% da sua renda.')
