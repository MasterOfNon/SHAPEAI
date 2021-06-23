import requests
import os.path
from datetime import datetime

api_key ="22a025edae7b1eb5d85a54bc186f5550"
location = input("Enter the city name: ")	
complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

temp_city = ((api_data['main']['temp']) - 273.15)
pressure = api_data['main']['pressure']
weather_desc = api_data['weather'][0]['description']
humdty = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print("--------------------------------------------------------")
print("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print("--------------------------------------------------------\n")
 
data = []
data.append("Current Temperature	: {:.2f} deg C\n".format(temp_city))
data.append("Current Weather Desc	: {}\n".format(weather_desc))
data.append("Current Humidity	: {}%\n".format(humdty))
data.append("Current Wind Speed	: {} kmph\n".format(wind_spd))
data.append("Current Pressure	: {} hPa\n".format(pressure))

for i in data:
	print(i)
	
def write_txt(x):
	with open("weather_data.txt", x) as f:
		f.write("\nWeather Stats for - {}  || {}\n".format(location.upper(), date_time))
		for i in data:
			f.write(i)
	
if os.path.isfile("weather_data.txt"):
	write_txt('a')
else:
	write_txt('w')
