## Program - AirWatch ##

## Disclaimer: This program might require to be runned twice for the menu to work in the terminal. ##

import os
os.system('cls' if os.name == 'nt' else 'clear')

from api import get_aircraft_data
from api import flights
from api import count_aircrafts_in_country

callsignInput = "Default"

print("\nActivating Program - AirWatch\n")

print("Select an option:\n 1. Via CallSign\n 2. See Total Count of Aircrafts in a Country\n 3. Exit")
input1 = input("\nEnter your choice: ")

if input1 == "1":
    callsignInput = input("\nEnter the CallSign of the Aircraft: ")
    CallSign = callsignInput
    get_aircraft_data(CallSign)

elif input1 == "2":
    country = input("\nEnter your county of choice: ")
    count_aircrafts_in_country(country)
    count = count_aircrafts_in_country(country)
    print("\nTotal Count of Aircrafts in " + country + ": " + str(count) + "\n")


else:
    print("\nExiting Program - AirWatch\n")

