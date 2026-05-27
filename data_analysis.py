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