#Soma de Ímpares Consecutivos II

n = int(input())

for i in range (n):
    x, y = (input().split(" "))
    if (x == y):
        print(0)
    elif (x > y):