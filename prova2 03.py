#Faça um algoritmo que lê valores para uma matriz W[5][6]. A seguir, inserir
#de forma compactada, num vetor U[30] os valores pares contidos em linhas de
#índice ímpar da matriz. No final, preencher os elementos restantes do vetor
#com o valor do somatório dos valores existentes entre 1 e os valores de seus
#índices.
def soma(b):
    sm=0
    for k in range(2,b):
        sm=sm+k
    return(sm)
w=[[0 for i in range (6)] for i in range (5)]
u=[0]*30
for l in range (5):
    for c in range(6):
        w[l][c]= int(input('DIGITE: '))
cont=0
acum=0
for l in range(5):
    if(l%2!=0):
        for c in range(6):
            if(w[l][c]%2==0):
                u[cont]=w[l][c]
                cont=cont+1
while(cont<=29):
    R=soma(cont)
    u[cont]=R
    cont+=1
for i in range(30):
    print('U [',i,'] = [',u[i],']')