#FUAQ lê o valor de compra de um produto. Calcular e
#mostrar a quantidade mínima de
#notas com que a compra pode ser paga, sabendo-se
#que o comprador dispõe apenas de
#notas de R$ 100, R$ 50, R$ 10 e R$ 1.
cp=float(input("valor da compra de um produto: "))
n1=cp/100
print("Quantidade de cedulas de R$100:",n1)
cp=cp-cp/100*100
n2=cp/50
print("Quantiade de cedulas de R$100:",cp/50)
cp=cp%50
n3=cp/10
print("Quantiade de cedulas de R$100:",cp/10)
cp=cp%10
n4=cp/1
print("Quantiade de cedulas de R$100:",cp/1)
cp=cp%1

print(n1,n2,n3,n4)