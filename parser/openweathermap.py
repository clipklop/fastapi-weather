import json

import requests

from models.model import Weather
from config import OWP_API_KEY


def get_weather(city_name: str, api_key: str, lang: str = 'ru') -> dict[str, str]:

    url = f"https://api.openweathermap.org/data/2.5/weather?&units=metric&q={city_name}&appid={api_key}&lang={lang}"
    r = requests.get(url).json()

    return r


if __name__ == '__main__':
    weather = get_weather(city_name='Moscow', api_key=OWP_API_KEY)
    print(weather)
    print(OWP_API_KEY)