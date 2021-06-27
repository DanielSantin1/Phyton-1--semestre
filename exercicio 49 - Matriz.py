#2) FUAQ lê valores para uma matriz M[2][3].
#Contar e mostrar quantos valores contidos na
#matriz possuem fatorial maior que 500.
#O cálculo do fatorial deve ser realizado numa função
def fatorial(x):
    status = 0
    f = 1
    for i in range(1,x+1):
        f=f*i
    print('fatorial de: ' , x , ' = ', f)
    if(f>500):
        status += 1
    return(status)
m=[[0 for i in range (3)] for i in range (2)]
count = 0
for l in range (2):
    for c in range (3):
        m[l][c]= int(input('Digite: '))
        result=fatorial(m[l][c])
        count += result 
print('QTD: ',count)