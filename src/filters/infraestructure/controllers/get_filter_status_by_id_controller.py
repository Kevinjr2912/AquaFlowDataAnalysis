from ...application import GetFilterStatusByIdUseCase
from fastapi import HTTPException

class GetFilterStatusByIdController:
  def __init__(self, get_filter_status_by_id_usecase: GetFilterStatusByIdUseCase):
    self.get_filter_status_by_id_usecase = get_filter_status_by_id_usecase
  
  async def execute(self, filter_id: str):
    try:
      return await self.get_filter_status_by_id_usecase.execute(filter_id=filter_id)
    except Exception as e:
      raise HTTPException(status_code=500, detail=f"Server error: {str(e)}")