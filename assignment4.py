# 1 Maximum of Three Numbers

def maximum(a, b, c):

    if a > b and a > c:
        print("Maximum Number is :", a)

    elif b > a and b > c:
        print("Maximum Number is :", b)

    else:
        print("Maximum Number is :", c)


maximum(10, 25, 15)

# 2 Distinct Elements from List

def distinct(l):

    new_list = []

    for i in l:
        if i not in new_list:
            new_list.append(i)

    return new_list


list1 = [1, 2, 2, 3, 4, 4, 5]

print("Distinct List :", distinct(list1))

# 3 Multiply All Numbers in List

def multiply(l):

    result = 1

    for i in l:
        result = result * i

    return result


numbers = [2, 3, 4]

print("Multiplication :", multiply(numbers))

# 4 Factorial Program

def factorial(n):

    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    return fact


num = int(input("Enter a number : "))

print("Factorial :", factorial(num))

# 5 Reverse a String

def reverse_string(s):

    return s[::-1]


text = input("Enter a string : ")

print("Reverse String :", reverse_string(text))


# 6 Number Within Range

def check_range(n):

    if n >= 1 and n <= 100:
        print("Number is within range")

    else:
        print("Number is outside range")


check_range(50)

# 7 Print Even Numbers from List

def even_numbers(l):

    print("Even Numbers are :")

    for i in l:
        if i % 2 == 0:
            print(i)


list2 = [1, 2, 3, 4, 5, 6, 7, 8]

even_numbers(list2)

# 8 Prime Number Check

def prime(n):

    count = 0

    for i in range(1, n + 1):

        if n % i == 0:
            count = count + 1

    if count == 2:
        print("Prime Number")

    else:
        print("Not Prime Number")


prime(7)

# 9 Count Upper and Lower Letters

def count_letters(s):

    upper = 0
    lower = 0

    for i in s:

        if i.isupper():
            upper = upper + 1

        elif i.islower():
            lower = lower + 1

    print("Upper Case Letters :", upper)
    print("Lower Case Letters :", lower)


count_letters("Hello World")

# File Handling

# Writing in file

file = open("demo.txt", "w")

file.write("Hello Python")

file.close()


# Reading file

file = open("demo.txt", "r")

print(file.read())

file.close()


# Appending in file

file = open("demo.txt", "a")

file.write("\nWelcome to Python")

file.close()
