from abc import ABC, abstractmethod
from typing import List
from ..dtos.output import HistoricalStatusFilterDTO, FilterStatusDTO

class LinearRegressionRepository(ABC):
  @abstractmethod
  def get_probability_layer_change(self, historical_status : HistoricalStatusFilterDTO, current_effectiveness: float) -> FilterStatusDTO: pass