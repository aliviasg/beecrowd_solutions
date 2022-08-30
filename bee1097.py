#Sequência IJ 3

J = 7

for i in range (1, 10, 2):
    for j in range(J,J-3,-1):
        print("I={} J={}".format(i, j))
    J = J + 2