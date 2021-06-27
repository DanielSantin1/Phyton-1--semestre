#FUAQ calculao consumo de combustível em uma viagem em um carro
#que faz media de 12km/L. Ler o tempo da viagem e a velocidade
#média. Calcule a distância utilizando a fórmula:
#D=V*T e o cosumo = D/12

T=float(input("tempo de viagem: "))
V=float(input("Velocidade média: "))

D=V*T
print('Foram {:.2f}'.format(D), 'Km De Distância')
D=D/12
print('Foram gastos {:.2f}'.format(D), 'De combustivel1')