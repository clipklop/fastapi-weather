import json

import requests

from models.model import Weather


def get_weather(city_name: str, lang: str = 'ru') -> dict[str, str]:
    api_key = "5617a2122cca993a3ddcbe401adb149d"

    url = f"https://api.openweathermap.org/data/2.5/weather?&units=metric&q={city_name}&appid={api_key}&lang={lang}"#lat={lat}&lon={lon}&appid={api_key}"
    # url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&appid={api_key}"
    
    return requests.get(url).json()


if __name__ == '__main__':
    weather = get_weather(city_name='Moscow')
    print(weather)