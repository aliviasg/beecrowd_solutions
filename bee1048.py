#Aumento de salário

salary_current = float(input())

if(0 < salary_current <= 400.00):
   readjustment = ((15 / 100) * salary_current)
   salary_new = salary_current + readjustment
   print("Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: 15 %".format(salary_new, readjustment))

elif(400.01 <= salary_current <= 800.00):
   readjustment = ((12 / 100) * salary_current)
   salary_new = salary_current + readjustment
   print("Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: 12 %".format(salary_new, readjustment))
elif(800.01 <= salary_current <= 1200.00):
    readjustment = ((10 / 100) * salary_current)
    salary_new = salary_current + readjustment
    print("Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: 10 %".format(salary_new, readjustment))
elif(1200.01 <= salary_current <= 2000.00):
    readjustment = ((7 / 100) * salary_current)
    salary_new = salary_current + readjustment
    print("Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: 7 %".format(salary_new, readjustment))
else:
    readjustment = ((4 / 100) * salary_current)
    salary_new = salary_current + readjustment
    print("Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: 4 %".format(salary_new, readjustment))