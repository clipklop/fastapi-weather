import json

import requests
# import typeshed

from config import load
from models.model import Weather


class OpenWeatherClient:
    def __init__(self, url: str, api_key: str) -> None:
        self.url = url
        self.api_key = api_key

    def get_weather(self, city_name: str, lang: str = 'ru') -> dict[str, dict | str | list] | None:

        if self.url is None or self.api_key is None:
            return None

        # self.url = self.url + \
        #     f"/weather?&units=metric&q={city_name}&appid={self.api_key}&lang={lang}"
        payload = {
            'q': city_name,
            'appid': self.api_key,
            'units': 'metric',
            'lang': lang
        }
        print(self.url)

        try:
            weather = requests.get(self.url, params=payload).json()
            return weather
        except requests.exceptions.RequestException as e:
            print(e)
            return None


if __name__ == '__main__':
    config = load()
    owc = OpenWeatherClient(config.openweather_url, config.openweather_api_key)
    weather = owc.get_weather(city_name='Moscow')
    print(weather)
