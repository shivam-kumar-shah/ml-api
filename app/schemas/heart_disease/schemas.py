from typing import List, Union
from pydantic import BaseModel


class PredictionInput(BaseModel):
    age: int
    sex: int
    cp: int
    trestbps: int
    chol: int
    fbs: int
    restecg: int
    thalach: int
    exang: int
    oldpeak: float
    slope: int
    ca: int
    thal: int

    def get_list(self) -> List[Union[int, float]]:
        return [
            self.age,
            self.sex,
            self.cp,
            self.trestbps,
            self.chol,
            self.fbs,
            self.restecg,
            self.thalach,
            self.exang,
            self.oldpeak,
            self.slope,
            self.ca,
            self.thal,
        ]
