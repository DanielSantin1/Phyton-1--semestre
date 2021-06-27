#FUAQ lê vaçpres para variáveis A e B.
#A seguir, trocar os valores entra as duas variáveis,,
#de forma que variável A passa a possuir o valor da
#Variavel B e variavel B passe a possuir o valor da variável A.
#no final mostrar as duas Variaveis A e B.

A=int(input('Digite um A nº: '))
B=int(input('Digite um B nº: '))
A, B = B, A
print('Váriavel A:',A, 'Variável B: ',B)
      