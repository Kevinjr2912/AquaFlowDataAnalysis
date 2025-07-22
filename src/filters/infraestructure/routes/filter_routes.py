from fastapi import APIRouter
from typing import List
from ..dependencies import get_water_quality_index_controller
from ...application import WaterQualityIndexDTO

filter_router = APIRouter()

@filter_router.get("/{filter_id}/water-quality-index", response_model=List[WaterQualityIndexDTO])
async def get_water_quality_index(filter_id: str):
    return await get_water_quality_index_controller.execute(filter_id)
