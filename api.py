## Connecting to an api using OpenSky-Network API-URL. ##
# Visit congif.py for more details. #

import requests

## This project requires installtion of the requests library. ##
## To install requests, run the following command in your terminal: "pip install requests" ##

from config import API_URL

request = requests.get(API_URL)

print("\nRequest status code: "+ str(request.status_code) +"\n")

flights = request.json().get("states")

CallSign = "UAL1777 "
def get_aircraft_data():
    for plane in flights:
        if plane[1] == CallSign:
            print("Data format - plane[1] = CallSign, plane[2] = Country of Origin, plane[3] = Last Position Update, plane[4] = Longitude, plane[5] = Latitude, plane[6] = Altitude, plane[7] = On Ground, plane[8] = Velocity\n")
            print("Data of the Aircraft with the CallSign " + CallSign + " is as follows:\n")
            print(plane[1], plane[2], plane[3], plane[4], plane[5], plane[6], plane[7], plane[8])
            print()
            return(plane[1], plane[2], plane[3], plane[4], plane[5], plane[6], plane[7], plane[8])
        else:
            print("No Aircraft with the CallSign " + CallSign + " was found.")
            return "No Aircraft with the CallSign " + CallSign + " was found."