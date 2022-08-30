#Experiências

tests = int(input())

c = 0
r = 0
s = 0
total = 0

for i in range(tests):
    amount, type_animal = (input().split(" "))
    amount = int(amount)

    total += amount

    if type_animal == "C":
        c += amount
    elif type_animal == "R":
        r += amount
    elif type_animal == "S":
        s += amount

rabbit_p = (c * 100.00) / total
rats_p = (r * 100.00) / total
frogs_p = (s * 100.00) / total

print("Total: {} cobaias".format(total))
print("Total de coelhos: {}".format(c))
print("Total de ratos: {}".format(r))
print("Total de sapos: {}".format(s))
print("Percentual de coelhos: {:.2f} %".format(rabbit_p))
print("Percentual de ratos: {:.2f} %".format(rats_p))
print("Percentual de sapos: {:.2f} %".format(frogs_p))