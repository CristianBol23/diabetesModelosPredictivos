from fastapi import APIRouter
from schemas.diabetes_schemas import PatientData, PatientDiabetesData
from services.diabetes_services import diabetes_prediction
router = APIRouter()

@router.post("/predict")
async def predict(data: PatientDiabetesData):
    #prediction = "Sano"
    prediction = diabetes_prediction(data)
    return{"prediction" : prediction}