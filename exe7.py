# Exercise 7:Sum of the First n Positive Integers
# Write a program that reads a positive integer, n, from the user and then displays the
# sum of all of the integers from 1 to n. The sum of the first n positive integers can be
# computed using the formula:
# sum = ((n)(n + 1))/2

num = int(input("Please enter a positive integer : "))
print("Sum of first ",num,"integers  is  :", int(num*(num+1)/2))

