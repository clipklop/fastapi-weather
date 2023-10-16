from datetime import datetime

import requests

from app.parser.models.model import Weather


class OpenWeatherClient:
    def __init__(self, url: str | None, api_key: str | None) -> None:
        self.url = url
        self.api_key = api_key

    def get_weather(self, city_name: str, lang: str = 'ru') -> dict[str, str] | None:

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


def weather_to_model(weather_dict: dict[str, str] | None) -> Weather | None:
    # Наверное не самое красивое решение, но мне показалось, что все эти поля будет
    # полезно тянуть и сохранять в датакласс для последующего анализа
    if not weather_dict:
        return None

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
        wind={
            'speed': weather_dict.get('wind').get('speed'),
            'deg': weather_dict.get('wind').get('deg'),
            'gust': weather_dict.get('wind').get('gust')
        },
        clouds={
            "all": weather_dict.get('clouds').get('all')
        },
        rain=weather_dict.get('rain') if weather_dict.get('rain') else None
    )
