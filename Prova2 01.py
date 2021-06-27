#Faça um algoritmo que lêvalores para as variáveis A e B. Consistir para que
#B recebe obrigatoriamenteum valor maior que A. Calcular e mostrar os fatoriais
#dos valores pares existentes entre A e B. Os cálculos de fatorial devem ser
#realizados dentro de uma função e os resultados mostrados no programa
#principal. No final, mostrar a média dos resultados dos fatoriais calculados.
def fatorial(z): 
    f=1 
    for x in range (1, i+1): 
        f = f * x 
    return(f)
cont=0
a=int(input('Digite A:'))
b=int(input('Digite B:'))
b=b-1
fat=0
med=0
while(b<=a):
    b=int(input('Digite B:'))
fat=0
for i in range(a, b+1):
   if(i%2==0):
       fat = fat + fatorial(i)
       print('Fatorial [',fat,']')
       cont=cont+1
med=fat/cont
print('Média de fatoriais', fat ,'/',cont ,'=', med)
        

        
    
    