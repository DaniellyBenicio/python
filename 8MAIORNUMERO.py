#Crie um programa que leia uma lista de números do usuário e exiba o maior número dessa lista.

print('Maior número!')
maior = ''

for i in range(1,6):
    num = (input('Informe um número: '))
    if len(num) > len(maior):
        maior = num
print('Maior número: ', maior)
