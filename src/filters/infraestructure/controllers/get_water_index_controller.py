from ...application import GetWaterQualityIndexUseCase
from fastapi import HTTPException

class GetWaterQualityIndexController:
  def __init__(self, get_water_quality_index_usecase: GetWaterQualityIndexUseCase):
    self.get_water_quality_index_usecase = get_water_quality_index_usecase
  
  async def execute(self, filter_id: str):
    try:
      result = await self.get_water_quality_index_usecase.execute(filter_id=filter_id)
      return result
    except Exception as e:
      raise HTTPException(status_code=500, detail=f"Server error: {str(e)}")