from fastapi import FastAPI, Query
import numpy as np
from enum import Enum
from pydantic import BaseModel
from typing import Union, Annotated


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
    return {"Hello": 'World'}


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


@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(max_length=50)] = None):
    # [OLD VER] -> "q: Union[str, None] = Query(default=None, max_length=50)"
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}
