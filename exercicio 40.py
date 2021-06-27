#FUAQ lê valores para um vetor X[5]. Após,
#encontrar e mostrar as seguintes informações:
#a) A média dos valores contidos nos elementos com
#índice ímpar; b) A média dos valores pares existentes no vetor;
#c) A quantidade de vezes que o
#valor 5 está presente nos elementos do vetor.

v=[0]*5
for i in range (5):
 v[i]=int(input('Digite um valor: '))
acum=0
cont1=0
for i in range (5):
 if(i%2==1):
     acum=acum+v[i]
     cont1=cont1+1
print('O somatorio é:',acum/cont1)
cont2=0
acum2=0
for i in range (5):
 if(i%2==0):
     acum2=acum2+v[i]
     cont2=cont2+1
print('O somatorio é:',acum2/cont2)

cont3=0
for i in range (5):
    if(v[i]==5):
     cont3=cont3+1
print(cont3)




