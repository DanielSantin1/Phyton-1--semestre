#2) FUAQ lê valores para 3 variáveis A, B e C. Mostrar os valores em ordem crescente.

a=int(input("valor de A: "))
b=int(input("valor de B: "))
c=int(input("valor de C: "))

if(a>c):
    x=c
    c=b
    b=x
if(a>b):
    x=b
    b=a
    a=x
if(b>c):
    x=c
    c=b
    b=x
print(a, b, c)