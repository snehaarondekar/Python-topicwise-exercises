# Exercise 33: Day Old Bread
#
# A bakery sells loaves of bread for $3.49 each. Day old bread is discounted by 60
# percent. Write a program that begins by reading the number of loaves of day old
# bread being purchased from the user. Then your program should display the regular
# price for the bread, the discount because it is a day old, and the total price. All of the
# values should be displayed using two decimal places, and the decimal points in all
# of the numbers should be aligned when reasonable values are entered by the user.

BREAD_PRICE = 3.49
DISCOUNTED_PRICE =0.60

n = int(input("Enter number of loaves :"))
regular_price = n * BREAD_PRICE
discount = regular_price * DISCOUNTED_PRICE
total = regular_price - discount

print("Regular price= %.2f"%regular_price,"Discount =%.2f"%discount,"Total=%.2f"%total)
