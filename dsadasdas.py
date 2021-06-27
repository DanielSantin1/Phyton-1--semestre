x=int(input("valor de x: "))
y=x-1
while(y<=x):
    y=int(input('digite y:'))
for i in range (x+1,y):
    for j in range(1,6):
        t=j*i
        print(j,'*',i,'=',t)
    print('=========')