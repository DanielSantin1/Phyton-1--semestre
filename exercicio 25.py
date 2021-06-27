#FUAQ lê 5 valores para uma variável X.
#No final, mostrar a média dos valores ímpares digitados para X.
#Utilizar o comando for.
cont=0
acum=0
for i in range(5):
    x=int(input("valor: "))
    if(x%2== 1):
        cont=cont+1
        acum=acum+x
        
print(acum/cont)