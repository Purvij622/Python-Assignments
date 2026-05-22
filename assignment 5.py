# 1 CSV File for Address Book

import csv

file = open("addressbook.csv", "w", newline="")

writer = csv.writer(file)

# Column Names
writer.writerow(["Name", "Address", "Mobile", "Email"])

# Taking data from user

for i in range(3):

    print("\nEnter Details of Person", i + 1)

    name = input("Enter Name : ")
    address = input("Enter Address : ")
    mobile = input("Enter Mobile : ")
    email = input("Enter Email : ")

    writer.writerow([name, address, mobile, email])

file.close()

print("\nCSV File Created Successfully")
#-----------------------------
# 2 DATABASE Practice
#----------------------------------

import sqlite3

# Create Database

conn = sqlite3.connect("college.db")

print("Database Created")


# Create Cursor

cur = conn.cursor()

# Create Tables

cur.execute("create table if not exists student(id integer, name text, city text)")

cur.execute("create table if not exists teacher(id integer, name text, subject text)")

cur.execute("create table if not exists course(id integer, course_name text, fees integer)")

print("Tables Created")

# Insert Records


cur.execute("insert into student values(1,'Akshat','Ahmedabad')")
cur.execute("insert into student values(2,'Rahul','Delhi')")

cur.execute("insert into teacher values(1,'Amit','Python')")
cur.execute("insert into teacher values(2,'Neha','Database')")

cur.execute("insert into course values(1,'AI',50000)")
cur.execute("insert into course values(2,'Data Science',60000)")

conn.commit()

print("Records Inserted")

# Select Operations


print("\nStudent Table")

res = cur.execute("select * from student")

for row in res:
    print(row)


print("\nTeacher Table")

res = cur.execute("select * from teacher")

for row in res:
    print(row)


print("\nCourse Table")

res = cur.execute("select * from course")

for row in res:
    print(row)

# Update Data


cur.execute("update student set city='Mumbai' where id=1")

conn.commit()

print("\nData Updated")

# Delete Data


cur.execute("delete from teacher where id=2")

conn.commit()

print("Data Deleted")

# Final Select


print("\nUpdated Student Table")

res = cur.execute("select * from student")

for row in res:
    print(row)


print("\nUpdated Teacher Table")

res = cur.execute("select * from teacher")

for row in res:
    print(row)


# Close Connection

conn.close()
