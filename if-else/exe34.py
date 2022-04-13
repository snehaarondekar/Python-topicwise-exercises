# Exercise 34: Even or Odd?
#
# Write a program that reads an integer from the user. Then your program should
# display a message indicating whether the integer is even or odd.
# ------------------------------------------------------------
# num = int(input("Enter a number :"))
# if num%2 == 0:
#     print(num,"is even")
# else:
#     print(num,"is odd")
# ----------------------------------------------------------
# Using ternary operator
# num = int(input("Enter a number :"))
# # print(num,"is even") if num%2 ==0 else print(num,"is odd")
# ------------------------------------------------------------
# Using Tuple
num = int(input("Enter a number :"))
print(("Odd","Even")[num%2 ==0])