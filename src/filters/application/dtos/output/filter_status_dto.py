from pydantic import BaseModel
from datetime import datetime

class FilterStatusDTO(BaseModel):
  status: float
  estimated_days: int
  probability_change: float
  estimated_day: datetime

