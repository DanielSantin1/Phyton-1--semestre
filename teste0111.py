def busca_binaria(v,p,r,x):
    if p <=r:
        q=(p+r)//2
        if x >v[q]:
            return busca_binaria(v,q+1,r,x)
        elif x < v[q]:
            return busca_binaria(v,p,q-1,x)
        else:
            return q
    return -1

vetor=[0]*10
chave=6
for i in range(10):
    vetor[i]=int(input('Digite um valor: '))
vetorOrdenado=sorted(vetor)
posicao = busca_binaria(vetorOrdenado, 0, len(vetorOrdenado)-1,chave)
if posicao >=0:
    print ('O elemento %d foi encotrado em %d.' %(chave,posicao))
else:
    print('O elemento %d não foi encontrado.'% chave)
print(vetor)
