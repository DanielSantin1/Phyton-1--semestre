#FUAQ lê valores para uma matriz M[2][3].
#A seguir, inserir de forma compactada os
#valores ímpares existentes na matriz num vetor V[6].
#Se restarem elementos vazios no vetor, preenche-los
#com o valor do seu índice.
#No final, mostrar o vetor.
v=[0]*6
m=[[0 for i in range (3)]for i in range(2)]
for l in range(2):
    for c in range(3):
        m[l][c]=int(input('Digite: '))
cont=0
cont2=0
for l in range(2):
    for c in range(3):
        if(m[l][c]%2==1):
            v[cont]=m[l][c]
            cont=cont+1
for j in range(6):
    v[j]=j
for i in range(6):
    print('v[',i,']=',v[i])

