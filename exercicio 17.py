#FUAQ lê valores para as variáveis A e B.
#Se A for par, calcular e mostrar o resto da divisão
#de A por B. Se A for ímpar e B for par,  trocar os
#soma das 3 variáveis
a=int(input("valor de a:"))
b=int(input("valor de b:"))

if(a %2==0):
        x=a%b
        print(x)
if(a%1 and b %2==0):
    x=a
    b=a
    x=b
if(a % 2==1 and b % 2==1):
    c=int(input("valor de c:"))
    y=a+b+c
    print(y)
    