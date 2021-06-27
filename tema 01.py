#1] FUAQ lê valores para uma variável X e uma variável Y. 
#Os valores devem ser lidos dentro de uma função que valida se o valor é maior que zero e menor que 100. 
#A seguir, contar e mostrar a quantidade de valores pares existentes entre X e Y.

def somatorio(var):
    acum=0
    for i in range(2,var):
        acum=acum+1
    return(acum)

a=int(input("Valor de A: "))
b=int(input("Valor de B: "))
soma=0
if(a%2==0):
    res=somatorio(a)
    print(res)
if(a%2==1 and b%2==0):
    res=somatorio(b)
    print(res)
if(a%2==1 and b%2==1):
    s=a+b
    res=somatorio(s)
    print(res)
