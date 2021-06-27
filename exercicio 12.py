#FUAQ lÊ as notas de duas provas de um aluno.
#após, calcular a média e msotrar a situação do aluno
#diante de três possibilidades: "Aprovado" com a média maior
#ou igual a 7.0, "EM exame" com médio menor que sete e igual
#ou maior que 3.0 e "reprovado" com média inferior a 3.0

n1=float(input('Digita a primeira nota:'))
n2=float(input('Digita a segunda nota:'))
med=(n1+n2)/2
if(med >=7.0):
    print("Aprovado")
if(med >= 3.0 and med <7.0):
    print("Em exame")
if(med<3.0):
    print("Reprovado")
    