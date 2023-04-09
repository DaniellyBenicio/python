#Crie um programa que leia uma lista de números do usuário e exiba o menor número dessa lista.
print('Menor número!')
menor = 100000000000000000

for i in range(1,6):
    num = int(input('Informe um número: '))
    if num < menor:
        menor = num
print('Menor número: ', menor)
