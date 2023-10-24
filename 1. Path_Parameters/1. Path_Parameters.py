from fastapi import FastAPI

#app = FastAPI() # FastAPI 클래스의 인스턴스 생성 -> HTTP 요청을 처리하고 응답을 생성하는데 사용됨


#@app.get("/items/{item_id}") # Path에서 동적으로 값을 가져옴
async def read_item(item_id): # item_id: 매개변수 또는 인자 (영어로 argument)
    return {"item_id": item_id} # 받은 값을 반환
