#FUAQ lê as duas notas, calcula e mostra a média semestral de cada
#aluno, para uma turma com 30 alunos. No final, mostrar a média
#Semestral mais alta da turma.
acum=0
for i in range(3):
    nt1=float(input('Prova 1: '))
    nt2=float(input('Prova 2: '))
    if(nt1>10):
        print("Digite para Prova 1 um valor de 0 a 10")
        nt1=float(input('Prova 1: '))
    if(nt2>10):
        print("Digite para Prova 2 um valor de 0 a 10")
        nt2=float(input('Prova 2 : '))
    if(nt1>=10 and nt2>=10):
        print("Digite para Prova 1 um valor de 0 a 10")
        print("Digite para Prova 2 um valor de 0 a 10")
        nt1=float(input('Prova 1: '))
        nt2=float(input('Prova 2: '))
    m=(nt1+nt2)/2
    print('Media do aluno : ',m)
    if(m>acum):
        acum=m
print('A media semestral mais alta é:', acum)