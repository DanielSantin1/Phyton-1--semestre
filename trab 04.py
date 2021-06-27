#4] FUAQ lê uma quantidade indeterminada de valores para a variável X.
#Quando for digitado o quarto valor PAR para X, encerrar a leitura e
#calcular e mostrar a média dos valores ímpares digitados para X.y=0
y=0
z=0

while(y<4):
    x=int(input('Digite X: '))
    if(x%2==0):
        y=y+1
        z=z+x
md=z/4
print('Media: ',md)