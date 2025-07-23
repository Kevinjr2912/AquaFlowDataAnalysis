from ...application import WeatherRepository
from pyowm.owm import OWM
from ....core.config import config

class Weather (WeatherRepository):
  async def get_temperature(self, city):
    owm = OWM(config.VITE_WEATHER_API_KEY)
    mgr = owm.weather_manager()
    observacion = mgr.weather_at_place(city)
    clima = observacion.weather

    return clima.temperature('celsius')['temp']

    