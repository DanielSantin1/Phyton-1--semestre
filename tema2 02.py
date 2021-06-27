#FUAQ lê valores para um vetor K[10]. Trocar a seguir, os
#valores dos elementos de índice par com os valores dos
#elementos de índice ímpar imediatamente seguintes. No final,
#mostrar o vetor K.
# Declara o vetor
k=[0]*10
# Le valores para o vetor
for i in range (10):
 k[i]=int(input())
# Troca valores do vetor
for i in range (9):
 if(i%2==0):
 x=k[i]
 k[i]=k[i+1]
 k[i+1]=x
# Mostra o vetor
for i in range (10):
 print(k[i]) 
