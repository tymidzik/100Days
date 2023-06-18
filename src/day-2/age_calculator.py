
# age calculator
age = int(input("What is your current age?\n"))

age_left = (90 - age)

days = age_left * 365

weeks = age_left * 52

months = age_left * 12

print(f"Youn have {days} days/{weeks} weeks/{months} months left")
