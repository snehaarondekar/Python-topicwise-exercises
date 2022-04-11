# Exercise 6:Tax and Tip
# The program that you create for this exercise will begin by reading the cost of a meal
# ordered at a restaurant from the user. Then your program will compute the tax and
# tip for the meal. Use your local tax rate when computing the amount of tax owing.
# Compute the tip as 18 percent of the meal amount (without the tax). The output from
# your program should include the tax amount, the tip amount, and the grand total for
# the meal including both the tax and the tip. Format the output so that all of the values
# are displayed using two decimal places.

TIP = 0.18
TAX = 0.11
meal_ammount = float(input("Enter ammount of the bill :"))
tip_ammount = meal_ammount * TIP #180
tax_ammount = meal_ammount * TAX #110
print("Grand total = %.2f" %(meal_ammount+tip_ammount+tax_ammount))