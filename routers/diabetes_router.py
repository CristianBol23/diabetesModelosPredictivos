from fastapi import APIRouter
from schemas.diabetes_schemas import PatientData, PatientDiabetesData, PatientDiabetesOutput
from services.diabetes_services import diabetes_prediction
router = APIRouter()

@router.post("/predict")
async def predict(data: PatientDiabetesData):
    #prediction = "Sano"
    prediction = diabetes_prediction(data)

    result = PatientDiabetesOutput(
        first_name=data.first_name,
        last_name=data.last_name,
        prediction=prediction
    )

    return{"prediction" : result}