import requests
import datetime
from pprint import pprint
from config import open_weather_token

def get_weather(city, open_weather_token):

    code_to_smile = {
        "Claer": "Clear \U00002600",
        "Clouds": "Clouds \U00002601",
        "Rain": "Rain \U00002614",
        "Drizzle": "Drizzle \U00002614",
        "Thunderstom": "Thunderstorm \U000026A1",
        "Snow": "Snow \U0001F328",
        "Mist": "Mist \U0001F32B"
    }

    try:
        # r = requests.get(f"https://api.gismeteo.net/v2/weather/current/4368/")
        r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric")
        data = r.json()
        # pprint(data)

        city = data["name"]

        smile_for_weather = data["weather"][0]["main"]
        if smile_for_weather in code_to_smile:
            smile = code_to_smile[smile_for_weather]
        else:
            smile = "Look at the window yourself)"

        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        lenght_of_the_sunday = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(data["sys"]["sunrise"])

        print(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
              f"Weather in {city} - {smile}: \n Temperature:{temperature} C\n Humidity:{humidity} %\n Pressure:{pressure} hPa\n"
              f" Wind:{wind} m/s\n Sunrise:{sunrise}\n Sunset:{sunset}\n Length of the sunday:{lenght_of_the_sunday}\n"
              f"Have a nice day!")
    except Exception as ex:
        print(ex)
        print('Check the city.')



def main():
    city = input('Enter town: ')
    get_weather(city, open_weather_token)

if __name__ == '__main__':
    main()
