#FUAQ lê valores para 2 vetores A e B, com 5 elementos cada.
#A seguir, inserir valores num vetor C, também com 5 elementos,
#aonde cada elemento conterá o resultado da subtração dos elementos
#correspondentes de A por B.No final, mostrar o vetor C.

a=[0]*5
b=[0]*5
c=[0]*5
for i in range(5):
     a[i]=int(input('Digite valor de a:'))
     b[i]=int(input('Digite valor de b:'))
for i in range (5):
    c[i]=a[i]-b[i]
    print('v[',i,']=',c[i])