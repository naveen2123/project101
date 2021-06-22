import requests

import json


api_key = "f58537ee0c2ad78fe8de8139d4cf28bb"
base_url = "https://api.openweathermap.org/data/2.5/weather?"
city_name = input("Enter city name : ")

complete_url = base_url +"q=" + city_name + "&appid=" + api_key

response = requests.get(complete_url)
x = response.json()
#file1 = open("CITYtemp.txt","x") ---This can be used to create a file if u directly want to create a file from python
file1= open("CITYtemp.txt","a")



if x["cod"] != "404":

	y = x["main"]

	current_temperature = y["temp"]

	current_pressure = y["pressure"]

	current_humidity = y["humidity"]

	
	z = x["weather"]

	
	weather_description = z[0]["description"]
    
    
    
	
	a=(" Temperature (in kelvin unit) = " +
					str(current_temperature) +
		"\n atmospheric pressure (in hPa unit) = " +
					str(current_pressure) +
		"\n humidity (in percentage) = " +
					str(current_humidity) +
		"\n description = " +
					str(weather_description))
    

    
    

    
   

    
    
else:
	print(" City Not Found ")

print(a)
file1.writelines("City:"+city_name+"/n"+a)
file1.close()
