valor = int(input('Qual valor vai sacar?'))
total = valor
ced = 50
totalcedula = 0

while True:
    if total >= ced:
        total -= ced
        totalcedula += 1
    else:
        if totalcedula > 0:
            print(f'Total de {totalcedula} cedulas de R${ced}')
        if ced == 50 :
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
            totalcedula = 0
        if total == 0:
            break

print('Volte Sempre.')