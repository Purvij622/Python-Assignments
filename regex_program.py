import re

print("----- Email Check -----")

email = input("Enter email : ")

if re.search("@", email):
    print("Valid Email")

else:
    print("Invalid Email")


print("\n----- Mobile Number Check -----")

mobile = input("Enter mobile number : ")

if len(mobile) == 10 and mobile.isdigit():
    print("Valid Mobile Number")

else:
    print("Invalid Mobile Number")


print("\n----- String Check -----")

text = input("Enter string : ")

if text.isalpha():
    print("Only Alphabets")

else:
    print("Invalid String")