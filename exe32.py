# Exercise 32: Sort 3 Integers
#
# Create a program that reads three integers from the user and displays them in sorted
# order (from smallest to largest). Use the min and max functions to find the smallest
# and largest values. The middle value can be found by computing the sum of all three
# values, and then subtracting the minimum value and the maximum value.

n1 = int(input("Enter 1st number :"))
n2 = int(input("Enter 2nd number :"))
n3 = int(input("Enter 3rd number :"))
minimum = min(n1,n2,n3)
maximum = max(n1,n2,n3)
print("minimum =", minimum,"maximum =",maximum)