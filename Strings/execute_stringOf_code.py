# Execute a String of Code in Python

# code = """a = 6+5
# print(a)"""


code ="""def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    return fact


print(factorial(5))"""

exec(code)
