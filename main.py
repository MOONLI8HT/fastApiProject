from fastapi import FastAPI, Query, Path, Body
from enum import Enum
from pydantic import BaseModel, Field
from typing import Union, Annotated
import time


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


class User(BaseModel):
    username: str
    full_name: str | None = None


class Item(BaseModel):
    name: str
    description: str | None = Field(
        default=None, title="The description of the item", max_length=300
    )
    price: float = Field(gt=0, description="The price must be greater than zero")
    tax: float | None = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                }
            ]
        }
    }

app = FastAPI()


@app.get("/")
async def root():
    return {"Hello": 'World'}


@app.put("/users/{user_id}")
async def read_user(
        user_id: int,
        item: Item,
        user: User,
        add_info: Annotated[int, Body()]
):
    results = {"item_id": user_id, "item": item, "user": user, 'info': add_info}
    return results


@app.post("/items/")
async def create_item(item: Item):
    return item


@app.get("/items/{item_id}/")
async def read_items(
        item_id: Annotated[
            int,
            Path(
                title="The ID of the item to get",
                description=f'''
                    {time.ctime()}
                    item_id
                        ge: >= больше или равно (greater than or equal)
                        le: <= меньше или равно (less than or equal)
                    size
                        gt: >  больше (greater than) 
                        lt: <  меньше (less than)
                ''',
                ge=0,
                le=1000
            )
    ],
    q: Annotated[
        str | None,
        Query(
            alias="item-query",         # Другие имена, псевдонимы
            title="Query string",       # Заголовок, название
            description='''
                Query string for the items 
                to search in the database 
                that have a good match
            ''',                        # Описание запроса
            min_length=3,               # Минимальный размер
            max_length=50,              # Максимальный размер
            pattern=r"^Hello",          # ReExp, Регулярное выражение
            deprecated=False,           # *Функционал устаревший или нет
            include_in_schema=True      # *Показать в схеме OpenAPI
        )
    ] = None,
    size: Annotated[
        float | None,
        Query(
            gt=0,
            lt=10.5
        )
    ] = None
):
    results = {"item_id": item_id}
    if q:
        results["items"].update({"q": q})
    if size:
        results["items"].update({"size": size})
    return results

