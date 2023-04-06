#Crie um programa que leia uma lista de palavras do usuário e exiba somente as palavras que começam com a letra "a".

palavras = []
for lista in range(1, 6):
    palavra = input('Informe uma palavra: ')

    palavras.append(palavra)

print("As palavras iniciadas com 'aA' o são: ")
for palavra in palavras:
    if palavra[0] == 'a' or palavra[0] == 'A':
        print(palavra)