print('Digite o valor de três retas que analisarei se poderá formar um triângulo:')
a = float(input('Digite primeiro valor:'))
b = float(input('Digite segundo valor:'))
c = float(input('Digite terceiro valor:'))
if a < b+c and b < c+a and c < b+a :
    print('Os valores citados podem formar um triãngulo ', end='')
    if a == b == c:
        print('Equilátero.')
    elif a != b !=c !=a:
        print('Escaleno.')
    else:
        print('Isoceles.')
else:
    print('Os valores citados não podem formar um triãngulo.')
