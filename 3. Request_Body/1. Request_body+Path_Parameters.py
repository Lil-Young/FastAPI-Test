from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()


@app.put("/items/{item_id}/{dssdffd}")
async def create_item(item_id: int, item: Item):
    '''**item.dict()에서 ** 는 딕셔너리의 언패킹 연산자이다.
    이 연산자는 딕셔너리 내의 모든 키-값 쌍을 분리하여 함수 호출 또는 다른 딕셔너리에 전달하는데 사용된다. '''
    return {"item_id": item_id, **item.dict()}
