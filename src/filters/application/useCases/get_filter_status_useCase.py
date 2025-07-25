from ..dtos.output import FilterStatusDTO, MeasurementDTO, HistoricalStatusFilterDTO
from ...domain import FilterRepository
from ...application.services import LinearRegressionService
from collections import defaultdict
from typing import List
from datetime import datetime

class GetFilterStatusByIdUseCase:
  def __init__(self, filter_repository: FilterRepository, linear_regression: LinearRegressionService):
    self.filter_repository = filter_repository
    self.linear_regression = linear_regression

  async def execute(self, filter_id: str) -> dict[str, object]:
    measurements = await self.filter_repository.get_measurements_by_filter_id(filter_id=filter_id)
    grouped = self.__group_measurements_by_day(measurements)

    historical_days = []
    effectiveness_per_day = []
    status_today = None

    for day, sensors in grouped.items():
      effectiveness = self.__calculate_effectiveness_for_day(sensors)
      if effectiveness is None:
        continue

      if day.date() == datetime.now().date():
        status_today = effectiveness
      else:
        historical_days.append(day)
        effectiveness_per_day.append(effectiveness)

    if status_today is None:
      raise Exception("There are no measurements for today")
    
    historical_status = HistoricalStatusFilterDTO(days=historical_days, effectiveness=effectiveness_per_day)

    filter_status = await self.linear_regression.execute(historical_status, status_today)

    return {
      "filter_status": filter_status,
      "historical_status_filter": historical_status
    }

  def __group_measurements_by_day(self, measurements: List[MeasurementDTO]) -> dict:
    grouped = defaultdict(dict)
    for m in measurements:
      grouped[m.day][m.name_sensor] = m.average_value
    return grouped

  def __calculate_effectiveness_for_day(self, sensors: dict) -> float | None:
    required_sensors = ["Ph", "Turbidity", "TDS", "Temperature"]
    if any(s not in sensors for s in required_sensors):
      return None

    ph = self.__calculate_effectiveness(9.5388, 7.2, sensors["Ph"])
    tds = self.__calculate_effectiveness(360.3146, 150, sensors["TDS"])
    turbidity = self.__calculate_effectiveness(25, 5, sensors["Turbidity"])

    return self.__calculate_total_effectiveness(ph, tds, turbidity)

  def __calculate_effectiveness(self, estimated_input: float, initial_output: float, average_output: float) -> float:
    denominator = estimated_input - initial_output

    if denominator == 0:
        return 1.0 if average_output == initial_output else 0.0

    effectiveness = (estimated_input - average_output) / denominator
    return max(0, min(effectiveness, 1))


  def __calculate_total_effectiveness(self, ph: float, tds: float, turbidity: float) -> float:
    weights = {
        "ph": 0.4286,
        "tds": 0.2857,
        "turbidity": 0.2857
    }

    def safe_pow(value: float, weight: float) -> float:
        return (value ** weight) if value > 0 else 0

    result = (
        safe_pow(ph, weights["ph"]) *
        safe_pow(tds, weights["tds"]) *
        safe_pow(turbidity, weights["turbidity"])
    ) * 100

    return result

