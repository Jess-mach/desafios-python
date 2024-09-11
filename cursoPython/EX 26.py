frase = str(input('Digite uma frase:')).upper().strip()
print('Analisando a frase {}, podemos concluir que:'.format(frase))
print('A letra "A" aparece {} veses.'.format(frase.count("A")))
print('A letra "A" aparace pela primeira vez na posição {}'.format(frase.find("A")+1))
print('A letra "A" aparace pela ultima vez na posição {}'.format(frase.rfind("A")+1))

