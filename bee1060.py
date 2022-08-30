#Números Positivos

count = 0
for item in range(6):
    number = float(input())
    if (number > 0):
        count += 1

print("{} valores positivos".format(count))