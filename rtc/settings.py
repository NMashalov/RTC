from pydantic_settings import BaseSettings
from functools import cache

class AppSettings(BaseSettings):
    host: str ='0.0.0.0'
    port:str ='8080'
    record_to: str ='records/'

@cache
def get_app_settings():
    return AppSettings()