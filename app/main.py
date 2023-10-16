from dataclasses import asdict

from fastapi import FastAPI

from app.parser.config import load
from app.parser.openweathermap import weather_to_model
from app.parser.openweathermap import OpenWeatherClient

app = FastAPI()


@app.get("/")
def read_root() -> str:
    return "Hello, Weather!"


@app.get("/weather/{city_name}")
def read_weather_name(city_name: str) -> dict[str, str | None]:
    config = load()
    owc = OpenWeatherClient(config.openweather_url, config.openweather_api_key)
    weather = owc.get_weather(city_name=city_name)
    model = weather_to_model(weather)

    return asdict(model)

# if __name__ == '__main__':
#     uvicorn.run(app, host='0.0.0.0', port=5000)
