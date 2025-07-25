from pydantic import BaseModel
from datetime import datetime
from typing import List

class HistoricalStatusFilterDTO(BaseModel):
  days: List[datetime]
  effectiveness: List[float]
