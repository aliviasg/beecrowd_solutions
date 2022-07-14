a, b, s = (input().split(" "))
a = int(a)
b = int(b)
s = int(s)

MaiorAB = ((a + b) + abs(a - b)) / 2
MaiorAB = int(MaiorAB)

if MaiorAB > s:
    print("{} eh o maior".format(MaiorAB))
else:
    print("{} eh o maior".format(s))