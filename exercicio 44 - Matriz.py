#FUAQ lê uma matriz X[4][4]. Calcular e mostrar a
#soma dos valores contidos na terceira coluna.

m=[[0 for i in range (4)]for i in range(4)]
for l in range(4):
    for c in range(4):
        m[l][c]=int(input('Digite: '))
acum=0
for l in range(4):
    acum=acum+m[l][2]
print('Somatorio:',acum)