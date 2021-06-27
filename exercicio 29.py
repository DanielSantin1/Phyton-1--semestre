#somatorio
#fuaq lê um valor para uma variável x. calcular e mostrar o somá
#torio dos numeros inteiros existentes entre 1 e x. utilizar FOR

x=int(input('digite x:'))
acum=0
for i in range(2,x):
    acum=acum+i
    
print('somatorio:',acum)