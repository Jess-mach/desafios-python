from datetime import date
atual = date.today().year
nasc = int(input('Digite seu ano de nascimento:'))
sexo = str(input('Digite seu sexo:')).upper()
if sexo == 'FEMININO':
    print('Não é necessario se alistar')
elif sexo == 'MASCULINO':
    idade = atual - nasc
    print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}.')
    if idade == 18:
        print('Você precisa se alistar IMEDIATAMENTE no Serviço Militar.')
    elif idade < 18:
        saldo = 18 - idade
        print(f'Ainda faltam {saldo} para se alistar no Serviço Militar.')
        ano =  atual + saldo
        print(f'Seu alistamento será em {ano}.')
    elif idade > 18:
        saldo = idade - 18
        print(f'Você Já deveria ter se alistado no Serviço Militar há {saldo} anos.')
        ano =  atual - saldo
        print(f'Seu alistamento foi em {ano}.')
else :
    print('Essa opção não está disponivél.Tente novamente.')
