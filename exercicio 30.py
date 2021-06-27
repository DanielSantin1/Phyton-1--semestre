#fatorial
#fuaq lê valor para uma variável y.
#calcular e mostrar o fatorial de y.

y=int(input('Digite y:'))
f=1
for i in range(1,y+1):
    f=f*i
print('Fatorial:',f)