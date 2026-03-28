from pydantic import BaseModel

class PatientData(BaseModel):
        first_name: str
        last_name: str

class PatientDiabetesData(BaseModel):
        first_name: str
        last_name: str
        pregnancies: int
        glucose: int
        blood_pressure: int
        skin_thickness: int
        insulin: int
        bmi: float
        diabetes_pedigree_function: float
        age: int
        
