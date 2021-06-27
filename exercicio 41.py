#FUAQ lê valores para um vetor V[5].
#A seguir, inserir apenas os valores pares existentes
#no vetor V num vetor W[5] de forma compactada.
#Se restarem elementos vazios em W, preenche-los com o valor zero.

v=[0]*5
w=[0]*5
for i in range (5):
    v[i]=int(input('Digite: '))
cont=0
for i in range (5):
    if(v[i]%2==0):
        w[cont]=v[i]
        cont=cont+1
for i in range(cont,5):
    w[i]=0

for i in range(5):
    print('w [',i,']=',w[i])
        
        