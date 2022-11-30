import requests
import tabulate
import os
import location
from datetime import datetime


location = "Toronto "

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid=c5713d40b765816f82149df396da7f7c"
api_link = requests.get(complete_api_link)
api_data = api_link.json()
print(api_data)

temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %y | %I:%M:%S %p")


print("Weather stats for - {} || {}".format(location.upper(), date_time))
print("Current temperature is: {:.2f} deg C".format(temp_city))
print("Current weather desc :",weather_desc)
print("Current Humidity :",hmdt, '%')
print("Current wind speed :",wind_spd , 'kmph')