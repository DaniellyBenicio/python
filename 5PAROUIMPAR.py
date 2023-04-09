#Crie um programa que leia um número do usuário e determine se esse número é par ou ímpar.

print('PAR ou iMPAR?')
num = int(input('Informe um número: '))
if num % 2 == 0:
    print(num, 'É PAR!')
else:
    print(num, 'É ÍMPAR!')
