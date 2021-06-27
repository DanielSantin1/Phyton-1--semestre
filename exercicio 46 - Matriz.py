#FUAQ lê uma matriz M[3][2]. Inserir num vetor V[6] os
#valores da matriz.No final, mostra o vetor

m=[[0 for i in range (3)]for i in range(2)]
for l in range(2):
    for c in range(3):
        m[l][c]=int(input('Digite: '))   
v=[0]*6
cont=0
for l in range(2):
    for c in range(3):
        v[cont]=m[l][c]
        cont=cont+1
        
for i in range(6):
    print('v[',i,']=',v[i])

    
