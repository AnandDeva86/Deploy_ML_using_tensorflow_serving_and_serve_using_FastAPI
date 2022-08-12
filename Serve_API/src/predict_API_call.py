import logging
import requests
from .Models import CarModel
from .utils import do_prediction

# -----------------------------------------------------------
# File name: predict_API_call.py
# Author: Anand Devarajan
# Date created: 07/08/2022
# Date last modified: 07/08/2022
# Python Version: >3.9
# -----------------------------------------------------------

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

class PredictAPI:
    """serve predictions from the served model"""
    def __init__(self):
        self.url = "http://model-deploy:8501/v1/models/saved_model/versions/1:predict"

    def predict_single_input(self,Cylinders:int,Displacement:float
                                   ,Horsepower:float,Weight:float
                                   ,Acceleration:float,Model_Year:int
                                   ,Europe:int,Japan:int
                                   ,USA:int) -> requests.models.Response:
        """ It handles individual car parameters and create a dict out of it """
        instance = {"instances": [[Cylinders,Displacement,Horsepower
                                    ,Weight,Acceleration,Model_Year
                                    ,Europe,Japan,USA]]}

        return do_prediction(self.url, instance)


    def predict_multiple_input(self, cars: list[CarModel]) -> requests.models.Response:
        """ It handles a list of CarModels and create a dict out of it """
        final_lst = []
        for car in cars:
            lst = [car.Cylinders,car.Displacement,
                   car.Horsepower,car.Weight,
                   car.Acceleration,car.Model_Year,
                   car.Europe,car.Japan,car.USA]
            final_lst.append(lst)
        # create a dict
        instance = {"instances": final_lst}
        return do_prediction(self.url,instance)