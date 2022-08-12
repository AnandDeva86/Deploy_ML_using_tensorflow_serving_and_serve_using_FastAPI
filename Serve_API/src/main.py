from http.client import HTTPException
import uvicorn
from fastapi import FastAPI, Response
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from typing import List

from .predict_API_call import PredictAPI
from .Models import CarModel



# -----------------------------------------------------------
# File name: main.py
# Author: Anand Devarajan
# Date created: 07/08/2022
# Python Version: > 3.9
# -----------------------------------------------------------


app = FastAPI(debug=True)
API_call = PredictAPI()

@app.get('/')
async def index():
    """It is the home page"""
    intro_str = {"Hi there": "This API is used to consume and then serve predictions from the served model"}
    return intro_str


@app.get('/predict/')
async def predict_single(Cylinders:int,Displacement:float
                                   ,Horsepower:float,Weight:float
                                   ,Acceleration:float,Model_Year:int
                                   ,Europe:int,Japan:int
                                   ,USA:int) -> JSONResponse:
    """It performs get request"""
    prediction = API_call.predict_single_input(Cylinders,Displacement
                                  ,Horsepower,Weight
                                  ,Acceleration,Model_Year
                                  ,Europe,Japan,USA)
    if prediction:
        json_compatible_item_data = jsonable_encoder(prediction.json())
        return JSONResponse(content=json_compatible_item_data)
    else:
        return JSONResponse(status_code=404,
                            content={"message": "Problem with processing the request"})



@app.post('/predict_multiple/')
async def predict_multiple(cars: List[CarModel]) -> JSONResponse:
    """It performs post request with list of CarModel """
    if cars is None:
        raise HTTPException(status_code=400,
                            detail="Please provide an valid data when calling this request.")

    prediction = API_call.predict_multiple_input(cars)

    if prediction:
        json_compatible_item_data = jsonable_encoder(prediction.json())
        return JSONResponse(status_code=200,
                            content=json_compatible_item_data)
    else:
        return JSONResponse(status_code=404,
                            content={"message": "Problem with processing the request"})


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)