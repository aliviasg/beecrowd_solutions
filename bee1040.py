#Média 3

n1, n2, n3, n4 = (input().split(" "))
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

med = ((n1*2) + (n2*3) + (n3*4) + (n4*1)) / 10

if(med >= 7):
    print("Media: {:.1f}\nAluno aprovado.".format(med))
elif(med < 5):
    print("Media: {:.1f}\nAluno reprovado.".format(med))
elif(5 <= med <= 6.9):
    n_exame = float(input())
    med_final = (n_exame + med) / 2
    print("Media: {:.1f}\nAluno em exame.\nNota do exame: {:.1f}".format(med, n_exame))
    if(med_final >= 5.0):
        print("Aluno aprovado.\nMedia final: {:.1f}".format(med_final))
    else:
        print("Aluno reprovado.\nMedia final: {:.1f}".format(med_final))
