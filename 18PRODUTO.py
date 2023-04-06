#Crie um programa que leia uma lista de números do usuário e exiba o produto desses números.

print('Encontre o produto dos números')
produto = 1

for i in range(1, 6):
    num = int(input('Digite um número: '))
    produto = produto * num
    
print('Produto: ', produto)