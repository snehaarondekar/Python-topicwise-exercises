# Exercise 5: Bottle Deposits
# In many jurisdictions a small deposit is added to drink containers to encourage people
# to recycle them. In one particular jurisdiction, drink containers holding one liter or
# less have a $0.10 deposit, and drink containers holding more than one liter have a
# $0.25 deposit.
# Write a program that reads the number of containers of each size from the user.
# Your program should continue by computing and displaying the refund that will be
# received for returning those containers. Format the output so that it includes a dollar
# sign and always displays exactly two decimal places.

ONE_LITER_OR_LESS = 0.10
MORE_THAN_ONE_LITER = 0.25

less = int(input("Enter number of small containers :"))
more = int(input("Enter number of big containers :"))
returns = (ONE_LITER_OR_LESS * less) + (MORE_THAN_ONE_LITER * more)
print("You will earn %.2f$" %returns)