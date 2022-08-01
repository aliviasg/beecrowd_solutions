# Seis números ímpares

number = int(input())

for i in range(number, (number + 12), 2):
    if(i % 2 != 0):
        print(i)
    elif(number % 2 == 0):
        odd = i + 1
        print(odd)