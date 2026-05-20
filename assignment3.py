# Assignment 3

# Q1 Dictionary, Tuple and Set


print("----- Dictionary -----")

student = {
    "name": "Akshat",
    "rollno": 21,
    "course": "Btech AI"
}

print(student)

print("\n----- Tuple -----")

t = (10, 20, 30, 40)

print(t)

print("\n----- Set -----")

s = {1, 2, 3, 4, 5}

print(s)

# Q2 Function for Math Operations

print("\n----- Math Operations -----")

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


print("Addition :", add(a, b))
print("Subtraction :", sub(a, b))
print("Multiplication :", multiply(a, b))
print("Division :", divide(a, b))

# Q3 Palindrome Number


print("\n----- Palindrome Number -----")

num = int(input("Enter a number : "))

temp = num
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

print("Reverse Number :", rev)

if temp == rev:
    print("Palindrome Number")

else:
    print("Not Palindrome Number")
