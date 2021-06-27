#FUAQ lê uma quantidade indeterminada de valores para a variável X,
#até que seja digitado um valor ímpar para X. Para cada X par lido, calcular
#e mostrar o fatorial de X. 
x=0
while(x%2==0):
    x=int(input('Digite um valor para x:'))
    if(x%2==0):
        f=1
        for i in range(1,x+1):
            f=f*i
        print('o fatorial é:',f)