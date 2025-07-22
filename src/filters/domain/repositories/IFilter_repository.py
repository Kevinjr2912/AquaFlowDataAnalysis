from abc import ABC, abstractmethod
from typing import Any

class FilterRepository(ABC):
    @abstractmethod
    def get_water_quality_index_by_filter_id(self, filter_id: str) -> Any:pass
