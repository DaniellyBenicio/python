#Crie um programa que leia uma lista de números do usuário e exiba o menor número dessa lista.

menor = 0

for i in range(1,6):
    num = int(input('Informe um número: '))
    if menor > num:
        menor = num
print('O maior número foi: ', menor)