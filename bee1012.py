A, B, C = (input().split(" "))
A = float(A)
B = float(B)
C = float(C)

area_triangulo = (A * C) / 2
area_circulo = 3.14159 * (C ** 2)
area_trapezio = ((A + B) * C) / 2
area_quadrado = B * B
area_retangulo = A * B

print("TRIANGULO: {:.3f}\nCIRCULO: {:.3f}\nTRAPEZIO: {:.3f}\nQUADRADO: {:.3f}\nRETANGULO: {:.3f}".format(area_triangulo, area_circulo, area_trapezio, area_quadrado, area_retangulo))