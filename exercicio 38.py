#FUAQ lê valores para um vetor V[5].
#A seguir, ler um valor para a variável X.
#Logo após, verificar se o valor de X está no vetor.
#Se estiver, mostrar a posição (índice) onde
#foi encontrado. Se não estiver, mostrar
#a mensagem “NÃO ESTÁ NO VETOR”.

v=[0]*5
for i in range(5):
    v[i]=int(input('Digite 5 valores:'))
x=int(input('Digite valores para X:'))
status=0
for i in range(5):
   
    if(v[i]==x):
        status=1
        print('Esta no vetor',i)
if(status==0):
    print('Não está no Vetor')