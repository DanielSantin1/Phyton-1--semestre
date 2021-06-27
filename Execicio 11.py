#FUAQ Exercicio 02
Apst=150
Va=80
Vt=Apst*Va
print('Valor Total Bruto',Vt)
Ac=Vt*0.035
print('Valor total a: {:.0f}'.format(Ac))
hip=40
print('Valor total b:',hip)
Sc=Vt*0.0145
print('Valor total c:',Sc)
Dt=(Vt-Ac-hip-Sc)*0.1
print('Valor total d: {:.2f}'.format(Dt))
Vtl=Vt-Dt-Ac-hip-Sc
print('Valor total Liquido: ',Vtl)
Ti=Dt+Ac+hip+Sc
print('Valor total dos descontos: {:.2f}'.format(Ti))

