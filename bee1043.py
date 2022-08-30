#Triângulo

A, B, C = (input().split(" "))
A = float(A)
B = float(B)
C = float(C)

# | b - c | < a < b + c
# | a - c | < b < a + c
# | a - b | < c < a + b
triangle1 = abs(B - C) < A < (B + C)
triangle2 = abs(A - C) < B < (A + C)
triangle3 = abs(A - B) < C < (A + B)

if triangle1 and triangle2 and triangle3 == True:
    print("Perimetro = {:.1f}".format(A + B + C))
else:
    area = 0.5 * (A + B) * C
    print("Area = {:.1f}".format(area))