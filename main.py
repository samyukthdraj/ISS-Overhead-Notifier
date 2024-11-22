import requests
from datetime import *
#import smtp
#import time
#mymail, mypass

LAT = 12.974800
LONG = 77.652573

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# # print(response)
# response.raise_for_status()
# data = response.json()
# # print(data)
# 

# iss_position = (longitude, latitude)
# print (iss_position)

def is_night():

    parameters = {
        "lat" : LAT,
        "lng" : LONG,
        "formatted" : 0, #to make it into 12 hour format
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) #get only the hour from date time
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour
    if time_now>=sunset or time_now<=sunrise:
        return True

def is_overhead():

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) #get only the hour from date time
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])

    if LAT-5 <= latitude <= LAT+5 and LONG-5 <= longitude <= LONG+5:
        #our position within +5 or -5 degrees from iss position.
        return True

#now we have to automate a mail to be sent to our own ids.



