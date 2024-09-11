num = int(input('Digite um número inteiro:'))
print('Agora escolha qual será a base de conversão:')
print('\033[31m[1]\033[0m para \033[31mBINARIO\033[0m')
print('\33[31m[2]\033[0m para \033[31mOCTAL\033[0m')
print('\033[31m[3]\033[0m para \033[31mHEXADECIMAL\033[0m')
conversao = str(input('Digite sua escolha:'))
if conversao == '1':
    print('O número {} em BINARIO é {}'.format(num,bin(num)[2:]))
elif conversao == '2':
    print('O número {} em OCTAL é {}'.format(num,oct(num)[2:]))
elif conversao == '3' :
    print('O número {} em HEXADECIMAL é {}'.format(num,hex(num)[2:]))
else:
    print('Opção inválida. Tente novamente.')