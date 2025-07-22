from pydantic import BaseModel
from datetime import datetime

class WaterQualityIndexDTO(BaseModel):
  day: datetime
  ica_value: float