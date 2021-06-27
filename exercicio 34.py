#FUAQ lê valores para as variáveis A e B.
#Se A for par, calcular e mostrar o
#somatório dos valores existente entre 1 e A.
#Se A for ímpar e B par, calcular e mostrar o
#somatório dos valores existentes entre 1 e B.
#Se A for ímpar e B ímpar, calcular e mostrar o
#somatório dos valores existente entre 1 e o resultado
#da soma de A com B.
#Os cálculos dos somatórios devem ser realizados dentro de
#uma função e os
#resultados mostrados no programa principal.
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

         
    