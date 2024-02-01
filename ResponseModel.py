from typing import Any

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

# Для использования EmailStr нужно добавить соответствующий модуль`pip install pydantic[email]`

app = FastAPI()


# Запускаем через терминал, используя следующий код
# uvicorn ResponseModel:app --reload

# Для проверки результата переходим в документацию
# http://127.0.0.1:8000/docs


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = 10.5
    tags: list[str] = []


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str | None = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None


class BaseUser(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None


class UserInNew(BaseUser):
    password: str


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The Bar fighters", "price": 62, "tax": 20.2},
    "baz": {
        "name": "Baz",
        "description": "There goes my baz",
        "price": 50.2,
        "tax": 10.5,
    },
}


@app.post("/items/")
async def create_item(item: Item) -> Item:
    return item


@app.get("/items/")
async def read_items() -> list[Item]:
    return [
        Item(name="Portal Gun", price=42.0),
        Item(name="Plumbus", price=32.0),
    ]


@app.post("/user/model1/", response_model=UserOut)
async def create_user(user: UserIn) -> Any:
    return user


@app.post("/user/model2/")
async def create_user(user: UserInNew) -> BaseUser:
    return user


@app.get(
    "/items/{item_id}/name",
    response_model=Item,
    response_model_include={"name", "description"},
)
async def read_item_name(item_id: str):
    return items[item_id]


@app.get(
    "/items/{item_id}/public",
    response_model=Item,
    response_model_exclude={"tax", "tags"}
)
async def read_item_public_data(item_id: str):
    return items[item_id]
