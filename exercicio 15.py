#FUAQ lê o salário fixo de um vendedor e o
#valor total das vendas efetuadas por ele durante um mês.
#Cada vendedor recebe além do salário fixo uma comissão #
#calculada sobre o valor total das vendas
#de acordo com a seguinte regra: 5% se o valor total
#das vendas ultrapassar R$ 20 mil no mês ou 2% se for igual ou inferior
#a R$ 20 mil. Calcular e mostrar o valor da comissão e o valor do salário total do vendedor.

s=float(input("Salário Fixo: "))
v=float(input("total de vendas: "))
x=20000
if(v>x):
    v=v*0.05
    print("valor da comição:",v)
    x=v+s
    print(x)
if(v<=x):
    v=v*0.02
    print("valor da comição:",v)
    x=v+s
    print("Salário do vendedor",x)

    

