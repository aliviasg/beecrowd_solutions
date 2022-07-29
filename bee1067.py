#Números impares

number = int(input())
for item in range(number + 1):
    if(item % 2 != 0):
        print("{}".format(item))