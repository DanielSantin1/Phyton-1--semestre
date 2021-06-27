#FUAQ lê 4 valores para uma variável y.
#Calcular e mostrar 50% de cada valor lido
#No final, mostrar a média dos resultados
#calculados menores que 10. Utilizar o comando while
cp=0
ap=0
cont=0
while(cont<4):
    y=float(input('Digite o valor:'))
    p=y*0.5
    if(p<10):
        ap=ap+p
        cp=cp+1
    print('porcentagens',p)
    cont=cont+1
m=ap/cp
print(ap)
print(cp)
print('media:',m)