# Maior e posição

c = 0
position = 0

for i in range(100):
    x = int(input())
    if (x > c):
        c = x
        position = i
print(c)
print(position + 1)
