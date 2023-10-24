from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_user_item(item_id: str, needy: str): # item_id, needy 매개변수는 필수적이다.
    item = {"item_id": item_id, "needy": needy}
    return item
