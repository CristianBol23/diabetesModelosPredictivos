from pydantic import BaseModel

class PatientData(BaseModel):
        first_name: str
        last_name: str

class PatientDiabetesData(BaseModel):
        first_name: str
        last_name: str
        pregnancies: int
        glucose: int
        bloodPressure: int
        skinThickness: int
        insulin: int
        bmi: float
        diabetespedigreefunction: float
        age: int
        
class PatientDiabetesOutput(BaseModel):
        first_name: str
        last_name: str
        prediction: str