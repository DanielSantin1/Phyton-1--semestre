#Fuaq lê valores para 3 Variaveis A B e C, inicialemte
#trocar os valores entre A e C . logo após, a variavel B,
#deve receber o resultado da multiplicação do valor inicial de A,
#pelo valor de B. no Final, mostrar as três variaveis Lidas

A=int(input('A:'))
B=int(input('B:'))
C=int(input('C:'))
X=A
A=C
C=X
X=C*B
B=X
print('Variavel A:',A,'Variavel B:',B,'Variavel C:',C)