# Exercise 31:Sum of the Digits in an Integer
# Develop a program that reads a four-digit integer from the user and displays the sum
# of the digits in the number. For example, if the user enters 3141 then your program
# should display 3+1+4+1=9.

num = int(input("Enter 4 digit number :"))
rem4 = num % 10
num = num // 10
rem3 = num % 10
num = num // 10
rem2 = num % 10
num = num // 10
rem1 = num % 10
num = num // 10
print(rem1,"+",rem2,"+",rem3,"+",rem4,"=",rem1+rem2+rem3+rem4)
