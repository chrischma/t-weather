import requests
import pync
import time
import os

city 	= "ENTER YOUR CITY HERE"
api_key = "ENTER YOUR OPEN WEATHER MAP API KEY HERE"

os.system('say Hier ist der Ausblick für die nächsten 7 Tage!')

url = f'https://api.openweathermap.org/data/2.5/onecall?lat=51.33962&lon=12.37129&daily&timezone=mez&appid={api_key}&units=metric'
data = requests.get(url).json()
all_days = {}

print("\n ✅ Anfrage erfolgreich!" )
print('\n   Hier kommt der Ausblick für sieben Tage!\n ')

i = 0
for result in data:
	entry = data['daily'][i]

	date = time.ctime(int(entry['dt']))
	date = date[:-14]

	temp_min = round(entry['temp']['min'])
	temp_max = round(entry['temp']['max'])
	humidity = entry['humidity']

	if humidity <= 40:
		humidity = "☀️ "
	elif (humidity > 40) and (humidity<70):
		humidity = "🌤️ "
	elif humidity >= 70:
		humidity = "🌦️ "

	all_days[date]=temp_max
	i+=1

	if i == 1: print ("                   max    min    ")
	print(f'  {date}: {humidity}   {temp_max}°C   {temp_min}°C   ')

hottest_day = max(all_days,key=all_days.get)
hottest_day_temp = round(all_days[max(all_days,key=all_days.get)])
current_temp = round(data['current']['temp'])
current_hum = data['current']['humidity']

pync.notify(f'Die Temperatur in Leipzig liegt bei {current_temp}°C \nbei einer Luftfeuchtigkeit von {current_hum}%.\n')
print(f'\n🐸 Aktuell: {current_temp}°C und {current_hum}% Luftfeuchtigkeit')
print(f'😍 Heißester Tag: {hottest_day} mit {hottest_day_temp}°C!')