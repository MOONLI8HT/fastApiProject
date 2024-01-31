from typing import Annotated

from fastapi import FastAPI, Header

app = FastAPI()


# Запускаем через терминал, используя следующий код
# uvicorn HeaderParam:app --reload

# Для проверки результата переходим в документацию
# http://127.0.0.1:8000/docs


@app.get("/items/")
async def read_items(
        strange_header: Annotated[
            str | None,
            Header(
                convert_underscores=False  # Пример: user_agent -> user-agent, False отключает такую конвертацию
            )
        ] = None
):
    return {"strange_header": strange_header}


@app.get("/tokens/")
async def read_items(
        x_token: Annotated[
            list[str] | None,   # Возможность получать несколько заголовков
                                # с одним и тем же именем, но разными значениями.
            Header()
        ] = None
):
    return {"X-Token values": x_token}
