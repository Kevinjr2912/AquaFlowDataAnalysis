from ..repositories import WeatherRepository

class WeatherService:
    def __init__(self, weather_repository: WeatherRepository):
        self.weather_repository = weather_repository

    async def execute(self, city: str) -> float:
        return await self.weather_repository.get_temperature(city)