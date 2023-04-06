#Crie um programa que leia uma lista de números do usuário e exiba a média desses números.

soma = 0

for i in range(1,6):
    num = int(input('Digite um número: '))
    soma = soma + num
media = soma/5

print('A média entre os números foi: ', media)
