import requests
import json

API_KEY = "daf"
MY_LAT = 42.333309  # 12.971599
MY_LNG = 69.621811  # 77.594566
url = "https://weatherbit-v1-mashape.p.rapidapi.com/forecast/hourly"

querystring = {"lat": MY_LAT, "lon": MY_LNG, "hours": 48}

headers = {
    "X-RapidAPI-Key": "sdfd",
    "X-RapidAPI-Host": "af-v1-mashape.p.dfa.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

data = response.json()

with open("weatherdata.json", "w") as file:
    json.dump(data, file)
