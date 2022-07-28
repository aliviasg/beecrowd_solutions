#Tempo de jogo com minutos

hi, mi, hf, mf = (input().split(" "))
hi = int(hi)
mi = int(mi)
hf = int(hf)
mf = int(mf)

time = ((hf * 60) + mf) - ((hi * 60) + mi)

if time <= 0:
    time += 24 * 60

ht = time // 60
mt = time % 60

print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(ht, mt))