from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root() -> str:
    return "Hello, Weather!"


@app.get("/weather/{city_name}")
def read_weather_name(city_name: str, q: str | None) -> dict[str, str | None]:
    return {"city_name": city_name, "q": q}
