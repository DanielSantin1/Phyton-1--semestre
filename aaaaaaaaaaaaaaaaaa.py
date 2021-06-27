cont=0
y=0
while(cont<6):
    x=int(input('Digite valor de X: '))
    cont=cont+1
    if(x>y):
        y=x
print('Maior numero digitado: ', y)