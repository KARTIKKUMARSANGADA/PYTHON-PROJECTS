import calendar

year = int(input("enter year:"))
month = int(input("enter month:"))

calc = calendar.month(year,month)
print(calc)
