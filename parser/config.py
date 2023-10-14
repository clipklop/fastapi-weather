import imp
import os
import dataclasses

from dotenv import load_dotenv

load_dotenv()


@dataclasses.dataclass
class Config:
    openweather_url: str | None
    openweather_api_key: str | None


def load() -> Config:
    return Config(
        openweather_url=os.getenv("OWP_URL"),
        openweather_api_key=os.getenv("OWP_API_KEY")
    )
