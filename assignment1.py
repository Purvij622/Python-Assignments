# Q1 Student Result Progra

print("----- Student Result -----")

name = input("Enter student name : ")
clas = input("Enter class : ")

s1 = int(input("Enter marks of subject 1 : "))
s2 = int(input("Enter marks of subject 2 : "))
s3 = int(input("Enter marks of subject 3 : "))
s4 = int(input("Enter marks of subject 4 : "))
s5 = int(input("Enter marks of subject 5 : "))

total = s1 + s2 + s3 + s4 + s5
per = total / 5

print("\nStudent Name :", name)
print("Class :", clas)
print("Total Marks :", total)
print("Percentage :", per)


# Q2 String Functions Program
print("\n----- String Functions -----")

str1 = input("Enter first string : ")
str2 = input("Enter second string : ")

s = str1 + " " + str2

print("\nConcatenated String :", s)

print("Lower Case :", s.lower())
print("Upper Case :", s.upper())
print("Title Case :", s.title())
print("Swap Case :", s.swapcase())
print("Capitalize :", s.capitalize())
print("Center :", s.center(40, '*'))
print("Count of a :", s.count('a'))
print("Endswith :", s.endswith('a'))
print("Find :", s.find('a'))
print("isalnum :", s.isalnum())
print("isdigit :", s.isdigit())
print("isnumeric :", s.isnumeric())
print("isspace :", s.isspace())
print("Replace :", s.replace('a', '@'))


# Q4 Assignment Operators


print("\n----- Assignment Operators -----")

a = 10

print("Initial value :", a)

a += 5
print("After += :", a)

a -= 2
print("After -= :", a)

a *= 3
print("After *= :", a)

a /= 2
print("After /= :", a)

a %= 4
print("After %= :", a)

a **= 2
print("After **= :", a)

a //= 2
print("After //= :", a)



# Q5 Grade Program


print("\n----- Grade Program -----")

name = input("Enter student name : ")

m1 = int(input("Enter marks of subject 1 : "))
m2 = int(input("Enter marks of subject 2 : "))
m3 = int(input("Enter marks of subject 3 : "))
m4 = int(input("Enter marks of subject 4 : "))
m5 = int(input("Enter marks of subject 5 : "))

total = m1 + m2 + m3 + m4 + m5
per = total / 5

if per >= 60:
    grade = "A"

elif per >= 50:
    grade = "B"

elif per >= 40:
    grade = "C"

elif per >= 33:
    grade = "D"

else:
    grade = "Fail"

print("\nStudent Name :", name)
print("Total Marks :", total)
print("Percentage :", per)
print("Grade :", grade)
