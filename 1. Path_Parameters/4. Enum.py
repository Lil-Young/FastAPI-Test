from enum import Enum
from fastapi import FastAPI

# str, Enum을 상속하는 서브 클래스 생성, str과 Enum을 상속해야 함수에서 값을 가져올 수 있다.
class ModelName(str, Enum): 
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}
