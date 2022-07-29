#Pares, Ímpares, Positivos e Negativos

count1 = 0
count2 = 0
count3 = 0
count4 = 0
for item in range(5):
    number = int(input())
    if(number % 2 == 0):
        count1 += 1
    if(number % 2 != 0):
        count2 += 1
    if(number > 0):
        count3 += 1
    if(number < 0):
        count4 += 1
print("{} valor(es) par(es)\n{} valor(es) impar(es)\n{} valor(es) positivo(s)\n{} valor(es) negativo(s)".format(count1, count2, count3, count4))