a, b, c = (input().split(" "))
a = int(a)
b = int(b)
c = int(c)

list = [a, b, c]
list.sort()

print("{}\n{}\n{}\n".format(list[0], list[1], list[2]))
print("{}\n{}\n{}".format(a, b, c))
