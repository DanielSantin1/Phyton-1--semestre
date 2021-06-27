#FUAQ lê a quantidade de horas e o valor da hora paga
#para um programador de programação. A seguir, calcular
#o salário bruto, o vaor de desconto do imposto de renda
# de 27%¨sobre o salário Bruto e o salário líquido.
# No final, mostar o salário Liquido.
y=int(input("Quantidade de horas por mês trabalhadas: "))
x=float(input("valor do salário por hora:"))
salB=(y*x)
salL=SalB-(SalB*0.27)
print(f'Salário Liquido é {SalL:.2f} R$')
