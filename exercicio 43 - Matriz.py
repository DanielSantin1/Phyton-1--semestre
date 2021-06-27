#FUAQ lê uma matriz M [3][4]. Calcular e mostrar o somatório dos
#valores contidos na segunda linha.

m=[[0 for i in range (3)]for i in range(4)]
for l in range(3):
    for c in range(4):
        m[l][c]=int(input('Digite: '))
acum=0
for c in range(4):
    acum+=m[1][c]
print('Somatorio:',acum)