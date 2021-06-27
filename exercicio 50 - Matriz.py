#3) FUAQ lê valores para uma matriz M[3,3].
#Inserir, a seguir, de forma compactada, o
#fatorial de cada valor par existente na
#matriz dentro um vetor V[9]. Se restarem
#elementos vazios no vetor, preenchê-los
#com o valor do seu próprio índice.
#Calcular o fatorial dentro de uma função.
#Declarar apenas variáveis locais.
def fatorial(x):
    status = 0
    f = 1
    for i in range(1,x+1):
        f=f*i
    print('fatorial de: ' , x , ' = ', f)
    if(f>500):
        status += 1
    return(status)
m=[[0 for i in range (3)] for i in range (3)]
v=[0]*9
count = 0
for l in range (3):
    for c in range (3):
        m[l][c]= int(input('Digite: '))
            if(m[l][c]%2==0):
                m[l][c]=v[]
                