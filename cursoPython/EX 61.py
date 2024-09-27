p = int(input('Digite o termo:'))
r = int(input('Digite a razão:'))
t = p
c = 1
while c <= 10:
    print(f'{t} - ', end='')
    t += r
    c += 1
print('Fim')