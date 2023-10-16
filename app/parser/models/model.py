import datetime
from dataclasses import dataclass, field


@dataclass
class Weather():
    city_name: str
    country: str
    sunrise: datetime.datetime
    sunset: datetime.datetime
    longitude: float
    latitude: float
    weather: str
    weather_description: str
    icon: str
    temperature: float
    feels_like: float
    temp_min: float
    temp_max: float
    pressure: int
    humidity: int
    sea_level: int
    grnd_level: int
    visibility: int
    checked_at: datetime.datetime
    wind: dict = field(default_factory=lambda: {'speed': float, 'deg': int, 'gust': float})
    rain: dict = field(default_factory=lambda: {'1h': float})
    clouds: dict = field(default_factory=lambda: {'all': int})
