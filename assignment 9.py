#------------------
# 1.regex_program.py
#-----------------

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


#---------------------------------
# 2.datetime_pandas.py
#--------------------------------
import pandas as pd
from datetime import datetime



now = datetime.now()

print(now)

print("\nYear :", now.year)
print("Month :", now.month)
print("Day :", now.day)

print("\n----- Date Conversion -----")

dates = ["2025-01-10", "2025-02-15", "2025-03-20"]

series = pd.to_datetime(dates)

print(series)

print("\n----- Create DataFrame with Dates -----")

data = {
    "Name": ["Akshat", "Rahul", "Neha"],
    "Date": pd.to_datetime(["2025-01-10", "2025-02-15", "2025-03-20"])
}

df = pd.DataFrame(data)

print(df)

#-------------------------------------
# 3.data_analysis.py
#-----------------------------------

import pandas as pd



data = {
    "Name": ["Akshat", "Rahul", "Neha", "Aman", None],
    "Age": [20, 21, None, 22, 23],
    "Marks": [85, 90, 88, None, 75],
    "City": ["Ahmedabad", "Delhi", "Mumbai", "Pune", None]
}

df = pd.DataFrame(data)


print(df)

print(df.isnull())

print(df.isnull().sum())


print("\n----- Data Cleaning -----")

df["Age"] = df["Age"].fillna(df["Age"].mean())

df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

df["Name"] = df["Name"].fillna("Unknown")

df["City"] = df["City"].fillna("Not Available")

print(df)


print("\n----- Data Analysis -----")

print("Average Marks :", df["Marks"].mean())

print("Maximum Marks :", df["Marks"].max())

print("Minimum Marks :", df["Marks"].min())

print("\nStudents with Marks Greater than 80")

print(df[df["Marks"] > 80])
