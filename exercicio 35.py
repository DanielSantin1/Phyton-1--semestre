#FUAQ lê valores para um vetor V com 6 elementos.
#Após completar a leitura do vetor,atualizar os elementos
#de índice par com o resultado da multiplicação do valor
#contido no elemento pelo valor do seu próprio índice.
#E atualizar os elementos de índice ímpar, com o valor
#contido no elemento imediatamente anterior.
#No final, mostrar o vetor.

v=[0]*6
for i in range (6):
    v[i]=int(input('Digite valor:'))
for j in range (6):
    if(j%2==0):
        v[j]=v[j]*j
    else:
        v[j]=v[j-1]
for j in range (6):
    print('v[',j,']=',v[j])
    