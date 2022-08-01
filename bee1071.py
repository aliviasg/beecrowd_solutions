# Soma de ímpares consecutivos I

x = int(input())
y = int(input())

start = min(x, y) + 1
stop = max(x, y)

if start % 2 == 0:
    start += 1
else:
    start += 0

sum = 0

for i in range(start, stop, 2):
    sum += i
print(sum)