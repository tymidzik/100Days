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
