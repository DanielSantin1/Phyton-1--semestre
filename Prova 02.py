#FUAQ lê valores para as variáveis X e Y. Consistir para que Y receba um
#valor maior que X. Calcular e mostrar a tabuada de 1 até 10 para os
#números ímpares existentes entre X e Y. 
x=int(input('Digite x: '))
y=x-1
while(y<=x):
    print('Digite para Y um valor maior que X')
    y=int(input('Digite y: '))
    for i in range(x,y+1):
        if(i%2!=0):
            for j in range(1,11):
                t=j*i
                print(j,'*',i,'=',t)