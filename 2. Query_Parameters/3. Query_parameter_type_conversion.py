from fastapi import FastAPI

app = FastAPI()

'''
url로
http://127.0.0.1:8000/items/foo?short=1
http://127.0.0.1:8000/items/foo?short=True
http://127.0.0.1:8000/items/foo?short=true
http://127.0.0.1:8000/items/foo?short=on
http://127.0.0.1:8000/items/foo?short=yes
쓸 수 있다.
'''


@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None, short: bool = False): #
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item
