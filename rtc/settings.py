from functools import cache

from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    host: str = "0.0.0.0"
    port: str = "8080"
    record_to: str = "records/"


@cache
def get_app_settings():
    return AppSettings()
