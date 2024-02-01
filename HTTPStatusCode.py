from fastapi import FastAPI, status
# можно starlette.status вместо fastapi.status

app = FastAPI()
# Запускаем через терминал, используя следующий код
# uvicorn HTTPStatusCode:app --reload

# Для проверки результата переходим в документацию
# http://127.0.0.1:8000/docs


@app.post("/items/", status_code=status.HTTP_201_CREATED)  # 201
async def create_item(name: str):
    return {"name": name}
