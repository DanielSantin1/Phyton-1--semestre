v=[0]*6
for i in range (6):
    v[i]=int(input('Digite valor para o vetor: '))
status=1
while (status!=0):
status=0
for i in range (5):
    if(v[i]>v[i+1]):
        x=v[i]
        v[i]=v[i+1]
        v[i+1]=x
        status=1
for i in range (6):
    print('v[',i,']=',v[i]) 