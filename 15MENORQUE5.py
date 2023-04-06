#Crie um programa que leia uma lista de números do usuário e exiba somente os números menores do que 5.

menor5 = []

for i in range(1, 11):
    num = int(input('Digite um número: '))
    if num < 5:
        menor5.append(num)
        
print('números menores que 5 informados: ')
for num in menor5:
    print(num)
