m=[[0 for i in range(3)]for i in range(2)]
for l in range(2):
    for c in range(3):
        m[l][c]=int(input('Digite: '))
cont=0
for k in range(5):
    x=int(input('Digite X: '))
    status=0
    for l in range(2):
        for c in range(3):
            if(x==m[l][c]):
                status=1
                cont=cont+1
                print('Esta na matriz na linha',l,'coluna',c)
            if(status==0):
                print('Nao esta na matriz')
print('Qtd de X na matriz = ',cont)