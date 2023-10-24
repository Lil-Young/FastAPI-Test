''' 모든 데이터 검증은 Pydantic에서 내부적으로 수행함 '''
''' 
/user/me 라는 경로와 /user/{me} 라는 경로가 있으면 
/user/me를 먼저 선언해야 한다. 그렇지 않으면 user/{me}에 me가 매핑이 될 것이다.
'''

from fastapi import FastAPI

app = FastAPI()


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}
