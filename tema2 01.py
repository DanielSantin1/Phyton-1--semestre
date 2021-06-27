#FUAQ lê valores para um vetor W[6]. Após, encontrar e
#mostrar o maior valor e a
#posição em que ele está no vetor.

W=[0]*6
for i in range (6):
 W[i]=int(input())
m=W[0]
p=0
for i in range (1,6):
 if (W[i]>m):
 m=W[i]
 p=i
print ('Maior eh ',m,' na posicao ',p)