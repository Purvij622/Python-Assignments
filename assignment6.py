

import requests
import random


# --------------------------------
# 1 Open Weather API Program
# ---------------------------------

city = input("Enter city name : ")

api_key = "ccdc8809884e46d9c43cf4a8ebb47bde"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)

weather = response.json()

print("\n----- Weather Details -----")

print("City :", weather["name"])
print("Temperature :", weather["main"]["temp"], "°C")
print("Feels Like :", weather["main"]["feels_like"], "°C")
print("Minimum Temp :", weather["main"]["temp_min"], "°C")
print("Maximum Temp :", weather["main"]["temp_max"], "°C")
print("Humidity :", weather["main"]["humidity"])
print("Pressure :", weather["main"]["pressure"])
print("Wind Speed :", weather["wind"]["speed"])
print("Weather :", weather["weather"][0]["description"])


# ---------------------------------
# 2 Stone Paper Scissor Game
# ---------------------------------

print("\n----- Stone Paper Scissor Game -----")

items = ["stone", "paper", "scissor"]

computer = random.choice(items)

user = input("Enter stone / paper / scissor : ")

print("Computer Choice :", computer)

if user == computer:
    print("Match Draw")

elif user == "stone" and computer == "scissor":
    print("You Win")

elif user == "paper" and computer == "stone":
    print("You Win")

elif user == "scissor" and computer == "paper":
    print("You Win")

else:
    print("Computer Wins")


# ---------------------------------
# 3 Free API Program
# ---------------------------------

print("\n----- Bitcoin Price API -----")

url = "https://api.coindesk.com/v1/bpi/currentprice.json"

response = requests.get(url)

bitcoin = response.json()

print("Updated Time :", bitcoin["time"]["updated"])

print("USD Rate :", bitcoin["bpi"]["USD"]["rate"])

print("GBP Rate :", bitcoin["bpi"]["GBP"]["rate"])

print("EUR Rate :", bitcoin["bpi"]["EUR"]["rate"])
