#FUAQ lê valores para as variáveis X e Y. 
#Se X for maior que Y, calcular e mostrar o
#resultado de Y multiplicado 5.
#Se X for igual a Y, calcular e mostrar o valor
#correspondente a 45% de Y.
#Se X for menor que Y, ler um  valor para Z e
#calcular e mostrar a soma entre as 3 variáveis.

x=float(input('x: '))
y=float(input('y: '))

if(x>y):
    y=y*5
    print(y)
if(x==y):
    y=y*0.45
    print(y)
if(x<y):
    z=int(input("z:"))
    a=x+y+z
    print(a)


