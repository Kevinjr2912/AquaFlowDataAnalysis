from abc import ABC, abstractmethod
from typing import Any

class FilterRepository(ABC):
    @abstractmethod
    def get_measurements_last_10_days_by_filter_id(self, filter_id: str) -> Any:pass
