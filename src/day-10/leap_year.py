def is_leap():
    if year % 4 == 0:
        if year % 100 != 0:
            leap_year = True
        elif year % 100 == 0 and year % 400 == 0:
            leap_year = True
        else:
            leap_year = False
    else:
        leap_year = False
    return leap_year


year = int(input("Which year do you want to check?\n"))
month = int(input("What month do you want to check?\n"))

month_days = ["31", "28", "31", "30", "31", "30", "31", "31", "30", "31", "30", "31", ]


def output():
    if month == 2 and is_leap():
        return "28"
    else:
        return month_days[month - 1]


print(output())
