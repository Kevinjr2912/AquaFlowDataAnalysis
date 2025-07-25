from typing import List
from ...application import MeasurementDTO
from ....core import database_conn
from ...domain import FilterRepository

class PostgreSQLFilter(FilterRepository):
    async def get_measurements_last_10_days_by_filter_id(self, filter_id: str) -> List[MeasurementDTO]:
        query = """
            SELECT 
              DATE(sr.recorded_at) AS day,
              sm.name_sensor,
              ROUND(AVG(sr.value), 2) AS average_value
            FROM sensors_readings sr
            JOIN sensors s ON sr.sensor_id = s.sensor_id
            JOIN sensors_models sm ON s.sensor_model_id = sm.sensor_model_id
            WHERE s.filter_id = :filter_id
              AND sr.recorded_at >= CURRENT_DATE - INTERVAL '11 days'
              AND sr.recorded_at < CURRENT_DATE
            GROUP BY sm.name_sensor, DATE(sr.recorded_at)
            ORDER BY day ASC, sm.name_sensor;
        """

        rows = await database_conn.fetch_all(query=query, values={"filter_id": filter_id})
        
        return [
            MeasurementDTO(
                day=row["day"],
                name_sensor=row["name_sensor"],
                average_value=row["average_value"]
            )
            for row in rows
        ]
    
    async def get_measurements_by_filter_id(self, filter_id: str) -> List[MeasurementDTO]:
        query = """
            SELECT 
              DATE(sr.recorded_at) AS day,
              sm.name_sensor,
              ROUND(AVG(sr.value), 2) AS average_value
            FROM sensors_readings sr
            JOIN sensors s ON sr.sensor_id = s.sensor_id
            JOIN sensors_models sm ON s.sensor_model_id = sm.sensor_model_id
            WHERE s.filter_id = :filter_id
              AND sr.recorded_at < CURRENT_DATE + INTERVAL '1 day'
            GROUP BY sm.name_sensor, DATE(sr.recorded_at)
            ORDER BY day ASC, sm.name_sensor;
        """

        rows = await database_conn.fetch_all(query=query, values={"filter_id": filter_id})
        
        return [
            MeasurementDTO(
                day=row["day"],
                name_sensor=row["name_sensor"],
                average_value=row["average_value"]
            )
            for row in rows
        ]
