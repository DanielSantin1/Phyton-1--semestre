#Faça um algoritmo que lê valores para uma matriz M[4][100]. Inserir, a
#seguir, o maior valor de cada linha, num vetor MVL[4]. No final, mostrar os
#valores contidos no vetor.
m=[[0 for c in range(100)] for l in range(4)]
v=[0]*4
for l in range (4):
    acum = 0
    for c in range (100):
        m[l][c]=int(input(f'Digite um valor M[{l+1}][{c+1}]: '))
        if(m[l][c] > acum):
            acum = m[l][c]
    v[l] = acum
for f in range(4):
    print('V[',f,'] => ', v[f])