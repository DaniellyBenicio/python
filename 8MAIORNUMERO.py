#Crie um programa que leia uma lista de números do usuário e exiba o maior número dessa lista.

print('Maior número!')
maior = 0

for i in range(1,6):
    num = int(input('Informe um número: '))
    if num > maior:
        maior = num
print('Maior número: ', maior)
