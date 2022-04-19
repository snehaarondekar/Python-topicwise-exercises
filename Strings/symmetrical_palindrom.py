# Python program to check whether the string is Symmetrical or Palindrome

# string = input("Enter string: ").strip().lower()
# mid = int(len(string)/2)
# start = 0
# end = len(string)-1
# if len(string) % 2 == 0:
#     for i, j in zip(range(start,mid), range(mid,end+1)):
#         if string[i] != string[j]:
#             print("String is not symmetrical")
#             break
#     else:
#         print("String is symmetrical")
# for i,j in zip(range(start,mid),range(end,mid,-1)):
#     if string[i] != string[j]:
#         print("String is not palindrome")
#         break
# else:
#     print("String is palindrome")

string = input("Enter string: ").strip().lower()
mid = int(len(string)/2)
start = 0
end = len(string)
if len(string)%2 == 0:
    str1 = string[start:mid]
    str2 = string[mid:end]
    if str1 == str2:
        print("String is symmetrical")
    else:
        print("String is not symmetrical")
else:
    print("String is not symmetrical")
str1 = string[::-1]
if str1 == string:
    print("String is palindrome")
else:
    print("String is not palindrome")





