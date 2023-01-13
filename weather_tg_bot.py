import requests
import datetime
from config import open_weather_token, tg_bot_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Hello! Where would you like to know the weather?")

@dp.message_handler()
async def get_weather(message: types.Message):
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
        r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric")
        data = r.json()


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

        await message.reply(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
              f"Weather in {city} - {smile}: \n Temperature:{temperature} C\n Humidity:{humidity} %\n Pressure:{pressure} hPa\n"
              f" Wind:{wind} m/s\n Sunrise:{sunrise}\n Sunset:{sunset}\n Length of the sunday:{lenght_of_the_sunday}\n"
              f"***Have a nice day!***")
    except:
        await message.reply('\U00002620 Check the city. \U00002620')


if __name__ == "__main__":
    executor.start_polling(dp)