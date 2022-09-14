from fastapi import FastAPI
from pydantic import BaseModel,validator
import pickle
import pandas as pd

app = FastAPI()

class PredictionItem(BaseModel):
    age: int
    sex: int
    bmi: float
    smoker: int

    @validator('sex')
    def passwords_match(cls, v):
        if v>1:
            raise ValueError('Please Enter 0 for female and 1 for male.')
        return v

    @validator('smoker')
    def name_must_contain_space(cls, v):
        if v>1:
            raise ValueError('Please Enter 0 for nonsmoker and 1 for smoker.')
        return v

with open('model.sav', 'rb') as f:
    model = pickle.load(f)

@app.post("/")
async def predict(item:PredictionItem):
    df=pd.DataFrame([item.dict().values()],columns=item.dict().keys())
    y = model.predict(df)*5000
    return {'Prediction': f'${round(y[0],2)}'}
