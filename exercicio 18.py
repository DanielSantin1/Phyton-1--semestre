#FUAQ lê valores paras as variáveis X e Y. Se X for maior que Y, calcular e mostrar a soma entre as duas variáveis. Se X e Y foram iguais, calcular e mostrar o valor correspondente a 30% de Y. Se X for menor
#que Y, trocar os valores entre X e Y.
x=int(input("valor de x:"))
y=int(input("valor de y:"))

if(x>y):
    s=x+y
    print(s)
if(x==y):
    s=y*0.3
    print(s)
if(x<y):
    a=x
    x=y
    y=a
    print(x,y)
    
