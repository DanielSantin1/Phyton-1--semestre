#FUAQ lê valores para as variáveis X e Y.
#Consistir para que Y receba obrigatoriamente um valor maior que X.
#Após, calcular e mostrar a tabuada de 1 até 5 dos
#valores inteiros existentes entre X e Y.
x=int(input("valor de x: "))
y=x-1
while(y<=x):
    y=int(input('digite y:'))
for i in range (x+1,y):
    for j in range(1,6):
        t=j*i
        print(j,'*',i,'=',t)

