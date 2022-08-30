# Médias ponderadas

n = int(input())

for i in range(n):
    a, b, c = (input().split(" "))
    a = float(a)
    b = float(b)
    c = float(c)
    total = ((a * 2) + (b * 3) + (c * 5)) / 10
    print("{:.1f}".format(total))