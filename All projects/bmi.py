import math
import sys

w = float(sys.argv[1])
h = float(sys.argv[2])
# w is weight in Kilograms and h is height in meters
bmi = w/(h**2)
if bmi < 15:
    print("Starvation")
elif bmi < 17.5:
    print("Anorexic")
elif bmi < 18.5:
    print("Underweight")
elif bmi > 40:
    print("Morbidly Obese")
elif 25 > bmi >= 18.5:
    print("Ideal")
elif 30 > bmi >= 25:
    print("Overweight")
elif 40< bmi <= 30:
    print("Obese")
