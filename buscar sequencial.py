def busca_sequencial(v,chave):
    p=0
    while(p<len(v)):
        if(chave==v[p]):
            return(p)
        p=p+1
    return(-1)

vetor=[0]*10

for i in range(10):
    vetor[i]=int(input('Digite valor: '))
    
valor=int(input('Digite o valor a ser procurado no vetor: '))

posicao=busca_sequencial(vetor,valor)

if(posicao>=0):
    print('O valor ',valor,' esta no vetor na posicao ',posicao)
else:
    print('O valor ',valor,' nao esta no vetor') 