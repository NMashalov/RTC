from pydantic_settings import BaseSettings
from functools import cache


class RTCSettings(BaseSettings):
    pass


@cache
def get_rtc_settings():
    return RTCSettings()
