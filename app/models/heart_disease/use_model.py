import pickle
from sklearn.linear_model import LogisticRegression
from os.path import join

from app.schemas.heart_disease.schemas import PredictionInput

# Pickle import
pkl_filename = join("app", "models", "heart_disease", "heart_disease.pkl")
with open(pkl_filename, "rb") as file:
    ml_model: LogisticRegression = pickle.load(file)


def get_prediction(input: PredictionInput) -> bool:
    prediction = ml_model.predict([input.get_list()])
    return bool(prediction[0])
