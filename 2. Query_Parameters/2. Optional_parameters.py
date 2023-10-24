from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None): # q는 선택적 매개변수
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}