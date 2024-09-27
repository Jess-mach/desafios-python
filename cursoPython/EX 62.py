p = int(input('Digite o termo:'))
r = int(input('Digite a razão:'))
t = p
c = 1
total = 0
mais = 10
while mais != 0 :
    total = total  + mais
    while c <= total:
        print(f'{t} - ', end='')
        t += r
        c += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostar a mais?'))
print(f'Progressão finalizada com {total} termos.')