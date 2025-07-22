from pydantic import BaseModel
from datetime import datetime

class MeasurementDTO(BaseModel):
  day: datetime
  name_sensor: str
  average_value: float