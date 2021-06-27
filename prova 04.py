#FUAQ lê 10 valores para a variável K. Verificar para cada K lido se o valor
#lido é um número perfeito ou não (um número perfeito é aquele que é
#igual à soma dos seus divisores). No final, mostrar a quantidade de
#números perfeitos que foram lidos.
cont=0
for i in range(10):
    k=int(input('digite um valor para k: '))
    acum=0
    for j in range(1,k):
        if(k%j==0):
            acum=acum+j
    if(acum==k):
     cont=cont+1
print('Quantida de Nº perfeitos',cont)
