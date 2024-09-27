#from math import factorial
#nun = int(input('Digite um número:'))
#print(f'Seu fatorial é {factorial(nun)}')

nun =  int(input('Digite um número para calcular seu Fatorial:'))
c = nun
f = 1
print(f'Calculando {nun}! = ', end='')
while c > 0:
  print(f'{c}', end='')
  print(' x ' if c>1 else ' = ', end='')
  f *= c
  c -= 1
print(f'{f}')
