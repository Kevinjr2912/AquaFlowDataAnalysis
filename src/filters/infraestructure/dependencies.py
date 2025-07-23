from .adapters import PostgreSQLFilter
from ..application import GetWaterQualityIndexUseCase
from .controllers import GetWaterQualityIndexController
from .adapters import Weather
from ..application.services import WeatherService

filter_repository = PostgreSQLFilter()
weather_repository = Weather()
weather_service = WeatherService(weather_repository=weather_repository)

# use cases
get_water_quality_index_usecase = GetWaterQualityIndexUseCase(filter_repository=filter_repository, weather_service=weather_service)

# controllers 
get_water_quality_index_controller = GetWaterQualityIndexController(get_water_quality_index_usecase=get_water_quality_index_usecase)

