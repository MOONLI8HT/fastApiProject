from datetime import datetime, time, timedelta
from uuid import UUID
from pydantic import Field
from fastapi import Body, FastAPI

app = FastAPI()
# Запускаем через терминал, используя следующий код
# uvicorn DataTypes:app --reload

# Для проверки результата переходим в документацию
# http://127.0.0.1:8000/docs


@app.put("/items/{item_id}")
async def read_items(
    item_id: UUID,
    start_datetime: datetime | None = Body(default=None),
    end_datetime: datetime | None = Body(default=None),
    repeat_at: time | None = Body(default=None),
    process_after: timedelta | None = Body(default=None),

):
    start_process = start_datetime + process_after
    duration = end_datetime - start_process
    return {
        "item_id": item_id,
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
        "repeat_at": repeat_at,
        "process_after": process_after,
        "start_process": start_process,
        "duration": duration,
    }


"""
UUID:
    Стандартный "Универсальный уникальный идентификатор", используемый в качестве идентификатора во многих базах данных и системах.
    В запросах и ответах будет представлен как str.
    
datetime.datetime:
    Встроенный в Python datetime.datetime.
    В запросах и ответах будет представлен как str в формате ISO 8601, например: 2008-09-15T15:53:00+05:00.
    
datetime.date:
    Встроенный в Python datetime.date.
    В запросах и ответах будет представлен как str в формате ISO 8601, например: 2008-09-15.
    
datetime.time:
    Встроенный в Python datetime.time.
    В запросах и ответах будет представлен как str в формате ISO 8601, например: 14:23:55.003.

datetime.timedelta:
    Встроенный в Python datetime.timedelta.
    В запросах и ответах будет представлен в виде общего количества секунд типа float.
    Pydantic также позволяет представить его как "Кодировку разницы во времени ISO 8601", см. документацию для получения дополнительной информации.
    
frozenset:
    В запросах и ответах обрабатывается так же, как и set:
    В запросах будет прочитан список, исключены дубликаты и преобразован в set.
    В ответах set будет преобразован в list.
    В сгенерированной схеме будет указано, что значения set уникальны (с помощью JSON-схемы uniqueItems).
    
bytes:
    Встроенный в Python bytes.
    В запросах и ответах будет рассматриваться как str.
    В сгенерированной схеме будет указано, что это str в формате binary.
    
Decimal:
    Встроенный в Python Decimal.
    В запросах и ответах обрабатывается так же, как и float.
"""