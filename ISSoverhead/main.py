import requests
import datetime
import smtplib
import time

MY_LAT = 12.971599
MY_LNG = 77.594566
my_email = "YOUR EMAIL HERE"
google_app_password = "PASSWORD"

url = 'http://api.open-notify.org/iss-now.json'
response = requests.get(url=url)
response.raise_for_status()
data = response.json()
iss_lng = float(data['iss_position']['longitude'])
iss_lat = float(data['iss_position']['latitude'])

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}
now = datetime.datetime.now()

r = requests.get(" https://api.sunrise-sunset.org/json", params=parameters)
r.raise_for_status()
data = r.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

while True:
    time.sleep(60)
    if MY_LAT-5 < iss_lng < MY_LAT+5 and MY_LNG - 5 < iss_lng < MY_LNG + 5:
        if now.hour > sunset or sunrise < sunrise:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=google_app_password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=my_email,
                    msg="Subject:ISS overhead look up\n\nlook around and find a light streak."
                )
                break
