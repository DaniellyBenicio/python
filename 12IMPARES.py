#Crie um programa que leia uma lista de números do usuário e exiba somente os números ímpares

impar = []

for i in range(1, 11):
    num = int(input('Digite um número: '))
    if num % 2 != 0:
        impar.append(num)
        
print('Os números ímpares informados são: ')
for num in impar:
    print(num)