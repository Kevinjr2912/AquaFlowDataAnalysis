from ..repositories import LinearRegressionRepository
from ..dtos.output import FilterStatusDTO, HistoricalStatusFilterDTO
from typing import List

class LinearRegressionService:
  def __init__(self, linear_regression: LinearRegressionRepository):
    self.linear_regression = linear_regression

  async def execute(self, historical_status: HistoricalStatusFilterDTO, current_effectiveness: float) -> FilterStatusDTO:
    return await self.linear_regression.get_probability_layer_change(historical_status=historical_status, current_effectiveness=current_effectiveness)