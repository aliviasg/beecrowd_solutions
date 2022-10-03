#Soma de Ímpares Consecutivos II

n = int(input())

for i in range(n):
    x, y = input().split(" ")
    x = int(x)
    y = int(y)

    soma = 0

    if(x > y):
        for j in range(x - 1, y, -1):
            if(j % 2 == 0):
                continue
            else:
                soma += j
    else:
        for j in range(x + 1, y):
            if(j % 2 == 0):
                continue
            else:
                soma += j
    print(soma)