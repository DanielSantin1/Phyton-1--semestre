#1) FUAQ lê uma matriz M[2][3].
#A seguir, ler 5 valores para uma variável X simples.
#Verificar para cada um dos X lidos se o valor está
#na matriz ou não. Se estiver, mostrar a posição
#(linha e coluna) em que foi encontrado.
#Senão, mostrar a mensagem “Não está na Matriz”.
#No final, mostrar a quantidade de X digitados
#que estavam na matriz.

m=[[0 for i in range (3)]for i in range(2)]
for l in range(2):
    for c in range(3):
        m[l][c]=int(input('Digite: '))
acum=0
for k in range(5):
    x=int(input('valor de x:'))
    cont=0
    for l in range(2):
        for c in range(3):
            if(x==m[l][c]):
                acum=acum+1
                print('Esta linha [',l,'] coluna [',c,']')
                cont=1
    if(cont==0):
        print('Não está na matriz')
print('Quantidade de x:',acum)        
        
                