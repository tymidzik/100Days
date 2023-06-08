# Bill calculator
print("Welcome to the bill calculator!")

total_bill = float(input("What was the total bill?\n"))

people = float(input("How many people to split the bill?\n"))

percent = float(input("What perfcentage tip would you like to give? 10, 12 or 15?\n"))

counting = "{:.2f}".format(total_bill * percent / 100 / people + total_bill, 2)

print(f"Ech person should pay: {counting}")

# digital numbers

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
# Write your code below this line 👇

first_number = int(two_digit_number[0])

second_number = int(two_digit_number[1])

sum = str(first_number + second_number)

first_number = str(two_digit_number[0])

second_number = str(two_digit_number[1])

print(first_number + " + " + second_number + " = " + sum)

# BMI calculator
weight = float(input("What is your weight?\n"))

height = float(input("How tall are you?\n"))

bmiResult = (weight / height ** 2)

weightstr = str(weight)

hightstr = str(height)

bmiResultStr = str(bmiResult)

print(weightstr + " / " + "(" + hightstr + "*" + hightstr + ")" + "=" + bmiResultStr)

bmiResultsInt = int(bmiResult)

print(bmiResultsInt)

# age calculator
age = int(input("What is your current age?\n"))

age_left = (90 - age)

days = age_left * 365

weeks = age_left * 52

months = age_left * 12

print(f"Youn have {days} days/{weeks} weeks/{months} months left")
