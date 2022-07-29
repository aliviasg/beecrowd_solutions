# Pares entre Cinco Números

count = 0
for item in range(5):
    number = int(input())
    if(number % 2 == 0):
        count += 1

print("{} valores pares".format(count))