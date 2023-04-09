#Crie um programa que leia um número do usuário e exiba a sua raiz quadrada.
from math import sqrt

print('Calculando a raiz quadrada')
num = int(input('Informe um número: '))

print('A raiz quadrada é = ', sqrt(num))

'''Outra forma de fazer sem usar o math, é utilizand o exponenciação.
>> raizq = num**0.5 
'''
