import json
from datetime import datetime   

import requests

from config import load
from models.model import Weather


class OpenWeatherClient:
    def __init__(self, url: str, api_key: str) -> None:
        self.url = url
        self.api_key = api_key

    def get_weather(self, city_name: str, lang: str = 'ru') -> dict[str, str]:

        if self.url is None or self.api_key is None:
            return None

        payload = {
            'q': city_name,
            'appid': self.api_key,
            'units': 'metric',
            'lang': lang
        }

        try:
            weather = requests.get(self.url, params=payload).json()
            return weather
        except requests.exceptions.RequestException as e:
            print(e)
            return None


def weather_to_model(weather_dict: dict[str, str]) -> Weather:
    return Weather(
        city_name=weather_dict.get('name'),
        country=weather_dict.get('sys').get('country'),
        sunrise=datetime.fromtimestamp(weather_dict.get('sys').get('sunrise')),
        sunset=datetime.fromtimestamp(weather_dict.get('sys').get('sunset')),
        longitude=weather_dict.get('coord').get('lon'),
        latitude=weather_dict.get('coord').get('lat'),
        weather=weather_dict.get('weather')[0].get('main'),
        weather_description=weather_dict.get('weather')[0].get('description'),
        icon=weather_dict.get('weather')[0].get('icon'),
        temperature=weather_dict.get('main').get('temp'),
        feels_like=weather_dict.get('main').get('feels_like'),
        temp_min=weather_dict.get('main').get('temp_min'),
        temp_max=weather_dict.get('main').get('temp_max'),
        pressure=weather_dict.get('main').get('pressure'),
        humidity=weather_dict.get('main').get('humidity'),
        sea_level=weather_dict.get('main').get('sea_level'),
        grnd_level=weather_dict.get('main').get('grnd_level'),
        visibility=weather_dict.get('visibility'),
        checked_at=datetime.fromtimestamp(weather_dict.get('dt')),
    )


if __name__ == '__main__':
    config = load()
    owc = OpenWeatherClient(config.openweather_url, config.openweather_api_key)
    weather = owc.get_weather(city_name='Moscow')
    print(weather)
    w = weather_to_model(weather)
    print(w)
