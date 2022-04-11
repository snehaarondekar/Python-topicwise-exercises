# Exercise 9: Compound Interest
# Pretend that you have just opened a new savings account that earns 4 percent interest
# per year. The interest that you earn is paid at the end of the year, and is added
# to the balance of the savings account. Write a program that begins by reading the
# amount of money deposited into the account from the user. Then your program should
# compute and display the amount in the savings account after 1, 2, and 3 years. Display
# each amount so that it is rounded to 2 decimal places.

INTEREST_RATE = 0.04
amount = float(input("Enter the Amount :"))
after_one_year = amount * INTEREST_RATE
amount = amount + after_one_year
print("Balance after 1 year = %.2f" %amount)
after_two_years = amount * INTEREST_RATE
amount = amount + after_two_years
print("Balance after 2 years =  %.2f" %amount)
amount_three_years = amount * INTEREST_RATE
amount = amount + amount_three_years
print("Balance after 3 years =  %.2f" %amount)