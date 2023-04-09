#Crie um programa que leia uma lista de números do usuário e exiba a lista ordenada em ordem decrescente.

ord = []

for i in range(1, 6):
    num = int(input('Informe um número: '))
    ord.append(num)
    
ord.sort(reverse=True)

print('Ordem decrescente: ', ord)