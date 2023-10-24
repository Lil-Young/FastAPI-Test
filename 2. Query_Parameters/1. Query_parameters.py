from fastapi import FastAPI

app = FastAPI()

fake_items_db = [
    {"item_name": "Foo"}, 
    {"item_name": "Bar"}, 
    {"item_name": "Baz"}
    ]

# default는 http://127.0.0.1:8000/members/?skip=0&limit=10 이고,
# url로 http://localhost:8000/items/?skip=0&limit=1를 치면 {"item_name": "Foo"} 값이 나온다.
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip+limit]
