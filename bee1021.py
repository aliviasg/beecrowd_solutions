x = float(input())

print("NOTAS:")
a = x % 100
r_a = (x - a) / 100
r_a = int(r_a)
print("{} nota(s) de R$ 100.00".format(r_a))

b = (a % 50)
r_b = (a - b) / 50
r_b = int(r_b)
print("{} nota(s) de R$ 50.00".format(r_b))

c = (b % 20)
r_c = (b - c) / 20
r_c = int(r_c)
print("{} nota(s) de R$ 20.00".format(r_c))

d = (c % 10)
r_d = (c - d) / 10
r_d = int(r_d)
print("{} nota(s) de R$ 10.00".format(r_d))

e = (d % 5)
r_e = (d - e) / 5
r_e = int(r_e)
print("{} nota(s) de R$ 5.00".format(r_e))

f = (e % 2)
r_f = (e - f) / 2
r_f = int(r_f)
print("{} nota(s) de R$ 2.00".format(r_f))

print("MOEDAS:")
t = (f % 1)
r_t = (f - t) / 1
r_t = int(r_t)
print("{} moeda(s) de R$ 1.00".format(r_t))

u = (t % 0.5)
r_u = (t - u) / 0.5
r_u = int(r_u)
print("{} moeda(s) de R$ 0.50".format(r_u))

v = (u % 0.25)
r_v = (u - v) / 0.25
r_v = int(r_v)
print("{} moeda(s) de R$ 0.25".format(r_v))

w = (v % 0.1)
r_w = (v - w) / 0.1
r_w = int(r_w)
print("{} moeda(s) de R$ 0.10".format(r_w))

y = (w % 0.05)
r_y = (w - y) / 0.05
r_y = int(r_y)
print("{} moeda(s) de R$ 0.05".format(r_y))

z = (y % 0.01)
r_z = (y - z) / 0.01
r_z = int(r_z)
print("{} moeda(s) de R$ 0.01".format(r_z))