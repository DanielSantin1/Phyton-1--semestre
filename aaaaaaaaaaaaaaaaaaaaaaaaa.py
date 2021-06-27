a=int(input('a: '))
b=int(input('b: '))
while(b<a):
    b=int(input('b: '))
acum=0
for i in range(a,b):
    if (i%2==0):
        acum=acum+i
print('Somatório dos valores pares: ', acum)