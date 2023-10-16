from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

app = FastAPI()

@app.post("/items/{item_id}")
async def create_item(item_id: int, name: str, description: str | None = None, price: float | None=None , tax: float | None = None, q: str | None = None):
    result = {"item_id": item_id, "name": name, "description": description, "price": price, "tax": tax }
    if q:
        result.update({"q": q})
    return result
