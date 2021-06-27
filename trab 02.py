#2 FUAQ lê valores para as variáveis X e Y.
#Consistir para que Y receba obrigatoriamente um valor maior que X.
#Após, calcular e mostrar oresultado da tabuada de 1 até 10 para
#cada um dos números inteiros entre X e Y.

x=int(input("valor de x: "))
y=int(input("valor de y: "))
if(y>x):
    acum=0 
for i in range(x,y):
    acum=i
    print('somatorio:',acum)
    for j in range(1,11):
        t=j*acum
        print(j,'*',i,'=> ',t)