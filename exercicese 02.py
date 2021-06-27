# FUAQ lê 6 valores para a variável K.
#Calcular e mostrar a média dos valores pares digitados para K e a
#quantidade de valores maiores que 100 digitados para K.
cont=0
acum=0
for i in range(6):
    k=int(input('Digite o valor: '))
    if(k%2==0):
        cont=cont+k
   
        print(cont)
        if(k>100):
            acum=acum+1
print(acum)
print(cont/6)