from abc import ABC, abstractmethod

class WeatherRepository(ABC):
  @abstractmethod
  def get_temperature(self, city: str) -> float:
    pass