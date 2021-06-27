for i in range(10):
    k=int(input('digite um valor para k'))
    acum=0
    for j in range(1,k):
        if(k%j==0):
            acum=acum+j
    if(acum==k):
        print('eh perfeito')
        