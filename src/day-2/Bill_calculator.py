# Bill calculator
print("Welcome to the bill calculator!")

total_bill = float(input("What was the total bill?\n"))

people = float(input("How many people to split the bill?\n"))

percent = float(input("What perfcentage tip would you like to give? 10, 12 or 15?\n"))

counting = "{:.2f}".format(total_bill * percent / 100 / people + total_bill, 2)

print(f"Each person should pay: {counting}")