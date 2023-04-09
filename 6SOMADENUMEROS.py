#Crie um programa que leia uma lista de números do usuário e exiba a soma desses números.

print('Soma de números')

soma = 0

for lista in range (1, 6):
    num = int(input('Informe valores: '))
    soma = soma + num

print('SOMA: ', soma)
