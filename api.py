## Connecting to an api using OpenSky-Network API-URL. ##
# Visit congif.py for more details. #

import requests

## This project requires installtion of the requests library. ##
## To install requests, run the following command in your terminal: "pip install requests" ##

from config import API_URL

request = requests.get(API_URL)

print("\n\nRequest status code: "+ str(request.status_code) +"\n")

flights = request.json().get("states")

CallSign = "Default"

def count_aircrafts_in_country(country):
    count = 0
    for plane in flights:
        if plane[2] and plane[2].strip() == country:
            count += 1
    return count

def get_aircraft_data(CallSign):
    found = False

    for plane in flights:

        if CallSign.strip() == plane[1].strip():
            print("Data of the Aircraft with the CallSign '" + CallSign.strip() + "' is as follows:\n")
            print( "CallSign: " + plane[1])
            print("Country of Origin: " + plane[2])
            print("Longitude: " + str(plane[5]))
            print("Latitude: " + str(plane[6]))
            print("On Ground: " + str(plane[8]))
            print("\n")
            found = True
        
    if not found:
            print("\n\nNo Aircraft with the CallSign " + CallSign + " was found.")
    

us_planes = count_aircrafts_in_country("United States")

