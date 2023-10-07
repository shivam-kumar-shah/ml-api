from fastapi import APIRouter

from app.schemas.heart_disease.schemas import PredictionInput
from app.models.heart_disease.use_model import get_prediction

router = APIRouter()


@router.post("/heart-disease/predict")
async def predict(input: PredictionInput):
    result = get_prediction(input)
    return {"result": result}
