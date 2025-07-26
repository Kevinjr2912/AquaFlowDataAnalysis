from .adapters import PostgreSQLFilter
from ..application import GetWaterQualityIndexUseCase
from .controllers import GetWaterQualityIndexController

filter_repository = PostgreSQLFilter()

# use cases
get_water_quality_index_usecase = GetWaterQualityIndexUseCase(filter_repository=filter_repository)

# controllers 
get_water_quality_index_controller = GetWaterQualityIndexController(get_water_quality_index_usecase=get_water_quality_index_usecase)

