# Exercise 43: Faces onMoney
# It is common for images of a country’s previous leaders, or other individuals of historical
# significance, to appear on its money. The individuals that appear on banknotes
# in the United States are listed in Table 2.1.
# Write a program that begins by reading the denomination of a banknote from the
# user. Then your program should display the name of the individual that appears on the
# Table 2.1 Individuals that appear on Banknotes
# Individual Amount
# George Washington $1
# Thomas Jefferson $2
# Abraham Lincoln $5
# Alexander Hamilton $10
# Andrew Jackson $20
# Ulysses S. Grant $50
# Benjamin Franklin $100
# banknote of the entered amount. An appropriate error message should be displayed
# if no such note exists.
# While two dollar banknotes are rarely seen in circulation in the United States,
# they are legal tender that can be spent just like any other denomination. The
# United States has also issued banknotes in denominations of $500, $1,000,
# $5,000, and $10,000 for public use. However, high denomination banknotes
# have not been printed since 1945 and were officially

individual_banknote = {1 :"George Washington",
                       2:"Thomas Jefferson",
                       5:"Abraham Lincoln",
                       10:"Alexander Hamilton",
                       20:"Andrew Jackson",
                       50:"Ulysses S. Grant",
                       100:"Benjamin Franklin"}
denomination_of_banknote = int(input("Enter value :"))
if denomination_of_banknote in list(individual_banknote.keys()):
    print(individual_banknote[denomination_of_banknote])
else:
    print("No such note exists")

