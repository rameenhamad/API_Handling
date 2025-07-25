import requests

url = "https://api.weatherstack.com/current?access_key=071c02b81b77fb92b3b3f7bff3168c2d"
CITY = input("enter city name")
querystring = {"query": CITY }
response = requests.get(url, params=querystring)
status = response.status_code
#print(response.json())
#use if to collect details wile status_code = 200:

data = response.json()

if status == 200:
    def general_info(a):
        city = a['name']
        country = a['country']
        time = a['localtime']
        print(f"city name: {city} \ncountry name: {country} \ntime & Date: {time}")
        #return city,country,time
        
    def weather_description(b):
        temprature = b['temperature']
        humidity = b['humidity']
        feellike = b['feelslike']
        cloudcover = b['cloudcover']
        wind_speed = b['wind_speed']
        weather_des = b['weather_descriptions']
        print(f"temprature: {temprature}°C \nhumidity: {humidity}% \nfeelslike; {feellike} \nDay Condition: {weather_des}")
        #return temprature,humidity,feellike, cloudcover, wind_speed, weather_des
    a = data['location']
    b = data['current']
    general_info(a)
    weather_description(b)
else:
    print("Check API response")
    