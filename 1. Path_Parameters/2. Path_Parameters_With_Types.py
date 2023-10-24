from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: int): # 매개변수에 type을 지정할 수 있다.
    return {"item_id": item_id}
