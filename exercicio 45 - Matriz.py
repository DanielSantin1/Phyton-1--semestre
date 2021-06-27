#FUAQ lê uma matriz M[2][3]. A seguir, ler um valor
#para a variável X. Após, verificar se X está na matriz ou não.
#Se estiver, mostrar a posição
#(linha e coluna) em que foi encontrado.
#Senão estiver, mostrar a mensagem “Não está na Matriz”.
m=[[0 for i in range (3)]for i in range(2)]
for l in range(2):
    for c in range(3):
        m[l][c]=int(input('Digite: '))
x=int(input('valor de x:'))
cont=0
for l in range(2):
    for c in range(3):
        if(x==m[l][c]):
            cont=cont+m[l][c]
            print('Esta linha [',l,'] coluna [',c,']')
            cont=1
if(cont==0):
    print('não está na Matriz')
    
