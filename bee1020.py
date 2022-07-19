days = int(input())

years = int(days / 365)
days -= years * 365

months = int(days / 30)
days -= months * 30

print("{} ano(s)\n{} mes(es)\n{} dia(s)".format(years, months, days))
