#Crie um programa que leia uma lista de palavras do usuário e exiba somente as palavras que começam com a letra "a".

lista_palavras = []
for i in range(1, 6):
    palavra = input('Informe uma palavra: ')

    lista_palavras.append(palavra)

print("As palavras iniciadas com 'aA' o são: ")
for palavra in lista_palavras:
    if palavra[0] == 'a' or palavra[0] == 'A':
        print(palavra)
