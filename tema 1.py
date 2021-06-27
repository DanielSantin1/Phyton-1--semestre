#1) FUAQ lê valores para as variáveis A, B, C e D. Encontrar e mostrar o maior valor dentre as 4 variáveis.
a=int(input("valor de A: "))
b=int(input("valor de B: "))
c=int(input("valor de C: "))
d=int(input("valor de D: "))

if(a>b and a>c and a>d):
    print(a)
if(b>a and b>c and b>d):
    print(b)
if(c>a and c>b and c>d):
    print(c)
if(d>a and d>b and d>c):
    print(d)

