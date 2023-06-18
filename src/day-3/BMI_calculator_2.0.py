#BMI calculator 2
weight = float(input("Enter your weight in kg:"))
height = float(input("Enter your height in m:"))

BMI = weight / height ** 2

print(f"{weight} / ({height} * {height}) = {BMI}")

if BMI < 18.5:
    print(f"Your BMI is {BMI} you are underweight.")
elif BMI >= 18.5 and BMI < 25:
    print(f"Your BMI is {BMI} you are normal weight.")
elif BMI >= 25 and BMI < 30:
    print(f"Your BMI is {BMI} you are slightly overweight.")
elif BMI >= 30 and BMI < 35:
    print(f"Your BMI is {BMI} you are overweight")
else:
    print(f"Your BMI is {BMI} you are clinically overweight")
