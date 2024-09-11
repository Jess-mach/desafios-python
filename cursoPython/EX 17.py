import math
co = float(input('Digite o valor do cateto oposto:'))
ca = float(input('Digite o valor do cateto adjacente:'))
hi = math.hypot(co, ca)
print('O comprimento do cateto oposto é {}, do adjacente é {} e sua hipotenusa é {:.2f}!'.format(co, ca, hi))