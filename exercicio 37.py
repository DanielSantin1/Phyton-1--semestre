#FUAQ lê valores para 2 vetores A e B, com 3 elementos cada.
#A seguir, inserir valores num vetor C que é a junção dos outros 2
#vetores, ou seja, que possui 6 elementos.
#No final, mostrar o vetor C.
a=[0]*3
b=[0]*3
c=[0]*6
for i in range(3):
     a[i]=int(input('Digite valor de a:'))
     b[i]=int(input('Digite valor de b:'))
for i in range (3):
    c[i]=a[i]
    c[i+3]=b[i]
for i in range (6):    
    print('v[',i,']=',c[i])