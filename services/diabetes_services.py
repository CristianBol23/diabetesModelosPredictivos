import pickle
from schemas.diabetes_schemas import PatientDiabetesData
import numpy as np

with open('RFDiabetesv132.pkl', 'rb') as file:
    RF_model2 = pickle.load(file)  

labels = ['Sano', 'Diabetes']

def diabetes_prediction(data: PatientDiabetesData):

    xin = np.array([
        data.pregnancies,
        data.glucose,   
        data.bloodPressure,
        data.skinThickness,
        data.insulin,
        data.bmi,
        data.diabetespedigreefunction,
        data.age
    ]).reshape(1,8)


    prediction = RF_model2.predict(xin)
    print("xin shape", xin.shape)
    return labels[prediction[0]]