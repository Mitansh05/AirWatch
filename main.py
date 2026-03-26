## Program - AirWatch ##

## Disclaimer: This program might require to be runned twice for the menu to work in the terminal. ##

import os
os.system('cls' if os.name == 'nt' else 'clear')


print("\nActivating Program - AirWatch\n")

print("Select an option:\n 1. Via CallSign\n 2. See Total Count of Aircrafts in a Country\n 3. Exit")
input1 = input("\nEnter your choice: ")

if input1 == "1":
    callsign = input("\nEnter the CallSign of the Aircraft: ")
elif input1 == "2":
    country = input("\nEnter your county of choice: ")