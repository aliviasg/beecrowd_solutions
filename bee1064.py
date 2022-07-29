# Positivos e Média

count = 0
total = 0.0
for item in range(1,7):
    number = float(input())
    if (number > 0):
        count += 1
        total += number
average = total / count

print("{} valores positivos\n{:.1f}".format(count, average))