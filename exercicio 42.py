#FUAQ lê valores para um vetor X[5].
#Após, inserir valores num vetor Y[5] de acordo com a seguinte
#regra: nos elementos de índice PAR, inserir o fatorial do VALOR
#contido no ELEMENTO CORRESPONDENTE EM X e nos elementos de índice
#ÍMPAR inserir o valor do próprio índice.
#Os cálculos dos fatoriais devem ser realizados numa função.

def fatorial(z):
    f=1
    for j in range(1,z+1):
        f=f*j
    return(f)

x=[0]*5
y=[0]*5
cont=0
acum=0
cont1=0
for i in range (5):
    x[i]=int(input('Digite: '))
    if(x[i]%2==0):
        y[i]=fatorial(x[i])
    else:
        y[i]=i
for i in range(5):
    print('w [',i,']=',y[i])