from dataclasses import asdict
from typing import Any

from fastapi import FastAPI

from app.parser.config import load
from app.parser.openweathermap import weather_to_model
from app.parser.openweathermap import OpenWeatherClient

app = FastAPI()


@app.get("/")
def read_root() -> str:
    return "Hello, Weather!"


@app.get("/weather/{city_name}")
async def read_weather_name(city_name: str) -> dict[Any, Any]: # dict[Any, Any] только так у меня это штука работает, иначе fastapi.exceptions.ResponseValidationError
    config = load()
    owc = OpenWeatherClient(config.openweather_url, config.openweather_api_key)
    # намучился с httpx, только в режиме async удалось эту штуку завести с fastapi
    weather = await owc.get_weather(city_name=city_name)

    model = weather_to_model(weather) # тут mypy ругается Argument 1 to "asdict" has incompatible type "Weather | None"; expected "DataclassInstance"  [arg-type], непонимаю как полечить
    return asdict(model)
