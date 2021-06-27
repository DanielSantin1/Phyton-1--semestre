#FUAQ lê valores para 3 variáveis A, B e C. Se a soma
#entre as 3 variáveis resultar num valor menor que 100
#ou maior que 200, trocar os valores entre A e B.Se não
#trocar os valores entra A e C. No final mostrar as 3
#variáveis Lidas
a=int(input('A:'))
b=int(input('B:'))
c=int(input('C:'))
x=a+b+c
if(x <100):
    y=a
    a=b
    b=y
else:
    y=a
    a=c
    c=y
print(a,b,c)
    
    
    
    