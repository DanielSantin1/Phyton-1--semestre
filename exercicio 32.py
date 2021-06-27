#FUAQ lê 6 valores para uma variável X.
#Verificar para cada X lido se ele é um valor
#par ou é ímpar.
#Se X for PAR, calcular e mostrar o SOMATÓRIO dos
#valores ímpares existentes entre 1 e X.
#Se X for ÍMPAR, calcular e mostrar o FATORIAL de X.
#Utilizar o comando while para fazer a
#leitura de 6 valores para X.
cont=0
while(cont<6):
    x=int(input("valor de x: "))
    cont=cont+1
    if(x%2==0):
        acum=0
        for i in range(2,x):
            if(i%2!=0):
                acum=acum+i
            print('o somatorio =',acum)
    else:
        f=1
        for j in range(1,x+1):
            f=f*j
            print('Fatorial:',f)