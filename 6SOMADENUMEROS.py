#Crie um programa que leia uma lista de números do usuário e exiba a soma desses números.

soma = 0

for lista in range (1, 6):
    num = int(input('Informe valores: '))
    soma = soma + num

print('A soma dos números é: ', soma)