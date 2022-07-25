cod, units = (input().split(" "))
cod = int(cod)
units = int(units)

if(cod == 1):
    price  = float(4.00 * units)
elif(cod == 2):
    price  = float(4.50 * units)
elif(cod == 3):
    price  = float(5.00 * units)
elif(cod == 4):
    price  = float(2.00 * units)
elif(cod == 5):
    price  = float(1.50 * units)
print("Total: R$ {:.2f}".format(price))