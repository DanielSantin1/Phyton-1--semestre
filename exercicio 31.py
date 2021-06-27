#FUAQ lê 5 valores para uma variável X.
#Verificar para cada X lido, se o valor é par ou é ímpar. Se for PAR,
#calcular e mostrar o somatório dos
#valores existentes entre 1 e X.
#Se X for ÍMPAR, calcular e mostrar a tabuada de 1 até 10 de X.
for i in range(5):
    x=int(input('Digite x:'))
    if(x%2==0):
        
        acum=0
        for i in range(2,x):
            acum=acum+i
        print('o somatorio =',acum)
    else:
        for k in range(1,11):
            t=k*x
            print(k,'*',x,'=>',t)