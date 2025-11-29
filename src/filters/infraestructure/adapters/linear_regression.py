from ...application.repositories import LinearRegressionRepository
from ...application.dtos.output import HistoricalStatusFilterDTO, FilterStatusDTO
from sklearn.linear_model import LinearRegression
from datetime import datetime, timedelta
import numpy as np

class Regression(LinearRegressionRepository):
  async def get_probability_layer_change(self, historical_status: HistoricalStatusFilterDTO, current_effectiveness: float) -> FilterStatusDTO:
    base_date = min(histaorical_status.days)

    X = np.array([(d - base_date).days for d in historical_status.days]).reshape(-1, 1)
    y = np.array(historical_status.effectiveness)

    model = LinearRegression()
    model.fit(X, y)

    threshold = 30

    slope = model.coef_[0]
    intercept = model.intercept_

    if slope == 0:
      days_from_base = float('inf')
    else:
      days_from_base = int((threshold - intercept) / slope)

    days_from_base = max(0, days_from_base)

    estimated_day = base_date + timedelta(days=days_from_base)

    today = datetime.now().date()
    estimated_days = max(0, (estimated_day.date() - today).days)

    if current_effectiveness > 100:
      probability = 0.0
    elif current_effectiveness < 30:
      probability = 1.0
    else:
      probability = 1 - ((current_effectiveness - 30) / (100 - 30))  

    return FilterStatusDTO(
      status=round(current_effectiveness, 2),
      estimated_days=estimated_days,
      probability_change=round(probability * 100, 2),
      estimated_day=estimated_day
    )
