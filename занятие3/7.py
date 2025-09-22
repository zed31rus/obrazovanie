def isleap(year):
    return True if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0) else False

year = int(input("year: "))

print(isleap(year))