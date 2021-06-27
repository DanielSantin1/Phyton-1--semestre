#FUAQ lê o salario fixo e o valor total das vendas
#realizadas pelo funcionário de uma loja. calcular a comissão
#e o salário total do vendedor considenrando que o valor de comissão
#é 5% sobre o valor total das vendas. No final, mostras o salário fixo
#o valor da comissão e o salário total.

s=float(input('Digite seu salário: '))
v=int(input('valor da venda: '))
c=v*0.05
x=(c*v)+s
print('Valor da comissão',c)
print('Valor do salário fixo',s)
print('Valor do Salário total',x)