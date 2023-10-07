import datetime
from dataclasses import dataclass, field


@dataclass
class Weather():
    city_name: str
    country: str
    sunrise: datetime.datetime
    sunset: datetime.datetime
    longitude: 37.6156
    latitude: 55.7522
    weather: 'Rain'
    weather_description: 'небольшой дождь'
    icon: '10d'
    temperature: 4.09
    feels_like: -0.76
    temp_min: 2.79
    temp_max: 4.65
    pressure: 993
    humidity: 91
    sea_level: 993
    grnd_level: 975
    visibility: 10000
    checked_at: datetime.datetime
    wind: dict = field(default_factory=lambda: {'speed': 7.27, 'deg': 179, 'gust': 15.22})
    rain: dict = field(default_factory=lambda: {'1h': 0.87})
    clouds: dict = field(default_factory=lambda: {'all': 100})
