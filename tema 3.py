#3) FUAQ lê valor para uma variável X. Se X for par, calcular e mostrar o valor correspondente a 45% de X.
#Se X for ímpar, ler um valor para a variável Y e calcular e mostrar o resultado da multiplicação de X por Y.


x=int(input("valor de x:"))

if(x %  2):
        y=int(input("valor de Y:"))
        x=x*y
        print(x)
else:
        x=x*0.45
        print(x)