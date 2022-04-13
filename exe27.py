# Exercise 27: Body Mass Index
# Write a program that computes the body mass index (BMI) of an individual. Your
# program should begin by reading a height and weight from the user. Then it should
# use one of the following two formulas to compute the BMI before displaying it. If
# you read the height in inches and the weight in pounds then body mass index is
# computed using the following formula:
# BMI = (weight/(height × height)) × 703.
# If you read the height in meters and the weight in kilograms then body mass index
# is computed using this slightly simpler formula:
# BMI = weight/(height × height).

sel = int(input("1) Inches and Pounds\n2) Meters and kgs\n"))
height = float(input("Enter Height :"))
weight = float(input("Enter Weight :"))
if sel == 1:
    print("BMI =",(weight/(height * height)) * 703)
elif sel == 2:
    print("BMI = %.2f"%(weight/(height * height)))
else:
    print("Invalid Input")
