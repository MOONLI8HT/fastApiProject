from fastapi import Cookie, FastAPI

app = FastAPI()
# Запускаем через терминал, используя следующий код
# uvicorn CookieParam:app --reload

# Для проверки результата переходим в документацию
# http://127.0.0.1:8000/docs
'''
    Объявляйте параметры cookie, 
    используя ту же структуру, 
    что и с Path и Query
'''


@app.get("/items/")
async def read_items(ads_id: str | None = Cookie(default=None)):
    return {"ads_id": ads_id}

"""
    Для объявления cookies, 
    вам нужно использовать Cookie, 
    иначе параметры будут интерпретированы 
    как параметры запроса.
"""
