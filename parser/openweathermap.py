import json

import requests

from models.model import Weather
from config import OWP_API_KEY, OWP_URL


class OpenWeatherClient:
    def __init__(self, url: str, api_key: str) -> None:
        self.url = url
        self.api_key = api_key

    def get_weather(self, city_name: str, lang: str = 'ru') -> dict[str, dict | str | list] | None:

        if self.url is None or self.api_key is None:
            return None

        self.url = self.url + \
            f"/weather?&units=metric&q={city_name}&appid={self.api_key}&lang={lang}"

        try:
            weather = requests.get(self.url).json()
            return weather
        except Exception as e:
            print(e)
            return None


if __name__ == '__main__':
    owc = OpenWeatherClient(OWP_URL, OWP_API_KEY)
    weather = owc.get_weather(city_name='Moscow')
    print(weather)
