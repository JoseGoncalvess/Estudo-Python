import calendar
print("="*15)


year = int(input("Qual Anodeseja ver?"))
month = int(input("Qual mês deseja ver?"))

print(calendar.month(year, month))

print(input('Deseja conferir mais algum mês?'))
