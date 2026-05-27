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