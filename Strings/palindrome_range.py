# Program to print all palindromes in a given range
nums = list(input("Enter range of numbers :").strip(" ").split(","))
n1 = int(nums[0])
n2 = int(nums[1])
for i in range(n1,n2+1):
    str_no = str(i)
    rev = str_no[::-1]
    if str_no == rev:
        print(i,end=" ")