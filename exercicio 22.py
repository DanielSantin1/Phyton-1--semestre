#FUAQ lê 5 valores para uma variável x. 
#Calcular e mostrar o valor correspondente
#a 50% de cada x lido. Usar o comando 'for'

cont=0
for i in range(5):
    x=int(input("valor:"))
    cont=cont+ 1
    print(x*0.5)