from typing import List
from collections import defaultdict
from ...domain import FilterRepository
from ..dtos.output import MeasurementDTO, WaterQualityIndexDTO
from ....utils import f_interp_ph, f_interp_turb, f_interp_tds, f_interp_temp

class GetWaterQualityIndexUseCase:
    def __init__(self, filter_repository: FilterRepository):
        self.filter_repository = filter_repository
        self.interp_ph = f_interp_ph()
        self.interp_turb = f_interp_turb()
        self.interp_tds = f_interp_tds()
        self.interp_temp = f_interp_temp()

    async def execute(self, filter_id: str) -> List[WaterQualityIndexDTO]:
        measurements: List[MeasurementDTO] = await self.filter_repository.get_measurements_last_10_days_by_filter_id(filter_id=filter_id)

        grouped_data = defaultdict(dict)
        for m in measurements:
            grouped_data[m.day][m.name_sensor] = m.average_value

        results: List[WaterQualityIndexDTO] = []

        for day, sensors in grouped_data.items():
            ph_avg = sensors.get("Ph")
            turbidez_avg = sensors.get("Turbidity")
            tds_avg = sensors.get("TDS")
            delta_temp_avg = sensors.get("Temperature")

            # print(f"Day: {day}, Ph: {ph_avg}, Turbidity: {turbidez_avg}, TDS: {tds_avg}, Temp: {temp_sample_avg}, DeltaTemp: {delta_temp}")

            if None in (ph_avg, turbidez_avg, tds_avg, delta_temp_avg):
                continue

            sub_ph = self.interp_ph(ph_avg)
            sub_turb = self.interp_turb(turbidez_avg)
            sub_tds = self.interp_tds(tds_avg)
            sub_temp = self.interp_temp(delta_temp_avg)

            
            # print(f"Interpolated values: ph={sub_ph}, turb={sub_turb}, tds={sub_tds}, temp={sub_temp}")

            # Pesos de cada parámetro (wi)
            w_ph = 0.3158
            w_temp = 0.2632
            w_turb = 0.2105
            w_tds = 0.2105

            # Cálculo del Índice de Calidad del Agua (ICA)
            ICA = ((sub_ph ** w_ph) * (sub_temp ** w_temp) * (sub_turb ** w_turb) * (sub_tds ** w_tds))

            results.append(WaterQualityIndexDTO(day=day, ica_value=round(ICA, 2)))

        return results

    def __interpolate(parameter, fun):
        
