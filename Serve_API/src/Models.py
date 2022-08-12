from pydantic import BaseModel

class CarModel(BaseModel):
    Cylinders: int
    Displacement: float
    Horsepower: float
    Weight: float
    Acceleration: float
    Model_Year : int
    Europe: int
    Japan: int
    USA: int