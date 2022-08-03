# Intervalo 2

n = int(input())

in_ = 0
out_ = 0

for i in range(0, n):
    x = int(input())
    if(10 <= x <= 20):
        in_+=1
    else:
        out_+=1
print("{} in".format(in_))
print("{} out".format(out_))