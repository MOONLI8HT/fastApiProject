from fastapi import FastAPI
import numpy as np
from enum import Enum
from pydantic import BaseModel
from typing import Union


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


app = FastAPI()

items = []


@app.get("/")
async def root():
    return {1: 1, "2": 2}


@app.get("/arange/{size}")
async def arange(size: int):
    result = list(np.arange(0, size, size / 10))
    return result


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    if not user_id.isdigit():
        return {"user_name": user_id}
    else:
        return {"user_id": user_id}


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


@app.post("/items/")
async def create_item(item: Item):
    return item


@app.post("/items/dict/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict
