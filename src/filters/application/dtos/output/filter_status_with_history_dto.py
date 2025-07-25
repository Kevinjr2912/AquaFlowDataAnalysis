from pydantic import BaseModel
from .filter_status_dto import FilterStatusDTO
from .historical_status_filter_dto import HistoricalStatusFilterDTO 

class FilterStatusWithHistoryDTO(BaseModel):
  filter_status: FilterStatusDTO
  historical_status_filter: HistoricalStatusFilterDTO