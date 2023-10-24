from fastapi import FastAPI

app = FastAPI()

# url을 http://localhost:8000/files/C/Users/exmaple.txt 쓸 수 있다.
# file_path:path에는 파일경로가 들어간다.
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}
