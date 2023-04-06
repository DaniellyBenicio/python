#Crie um programa que leia uma lista de números do usuário e exiba somente os números maiores do que 10.

maior10 = []

for i in range(1, 11):
    num = int(input('Digite um número: '))
    if num > 10:
        maior10.append(num)
        
print('números maiores que 10 informados: ')
for num in maior10:
    print(num)