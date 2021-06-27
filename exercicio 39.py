#FUAQ lê valores para um vetor x[6]. Após, calcular
#e mostrar o somatório dosvalores contidos nos
#elementos de índice ímpar.

v=[0]*6
for i in range (6):
 v[i]=int(input('Digite um valor: '))
acum=0
for i in range (6):
 if(i%2==1):
     acum=acum+v[i]
print('O somatorio é:',acum)
 
        
        
