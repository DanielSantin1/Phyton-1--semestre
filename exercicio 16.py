#FUAQ lê o salário fixo e a quantidade de linhas codificadas por um programador de computador durante um mês.
#O programador recebe, além do salário fixo, uma comissão calculada sobre o próprio salário fixo de acordo com
#a seguinte regra: 10% se o total de linhas codificadas for igual ou menor que 20 mil, 15% se for maior que 20 mil
#e menor que 50  mil e 20% se for igual ou maior que 50 mil linhas codificadas.
#O salário líquido é calculado, primeiro, por meio do salário bruto que é a soma do salário fixo com o valor
#da comissão e, em segundo lugar, por meio da subtração do salário bruto pelo valor de imposto, sendo esse último
#igual a 27% da soma do salário fixo com 50% da comissão. Calcular e mostrar o valor da comissão, o salário bruto,
#o valor do imposto e o salário líquido.

x=float(input("Salário fixo: "))
y=int(input("quantidade de linhas codificadas: "))

if(y<=20000 ):
    vc=x*0.10
if(y>20000 and y<50000):
    vc=x*0.15
if(y>=50000):
    vc=x*0.20
print(vc)
sb=x+vc
imp=(x+vc*0.5)*0.27
print("salário bruto",sb)
print("valor do imposto",imp)
print("Salário Liquido",sb-imp)

