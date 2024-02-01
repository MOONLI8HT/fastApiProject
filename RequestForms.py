from typing import Annotated

from fastapi import FastAPI, Form

# Для использования форм необходимо установить модуль
# `pip install python-multipart`

app = FastAPI()


# Запускаем через терминал, используя следующий код
# uvicorn RequestForms:app --reload

# Для проверки результата переходим в документацию
# http://127.0.0.1:8000/docs


@app.post("/login/")
async def login(
        username: Annotated[str, Form()],
        password: Annotated[str, Form()]
):
    return {"username": username, "password": '*' * len(password)}

#  чтение форм через application/x-www-form-urlencoded
