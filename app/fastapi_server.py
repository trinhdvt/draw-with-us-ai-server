import uvloop
from fastapi import FastAPI, UploadFile

from app.exception_handler import add_exception_handler
from app.middleware_config import add_middleware
from app.model import RequestModel
from app.utils import preprocess_str, predict

app = FastAPI()
add_middleware(app)
add_exception_handler(app)
uvloop.install()


@app.get("/ping")
@app.get("/")
async def root():
    return {"message": "OK"}


@app.post("/predict/v1")
async def predict_base64(req: RequestModel):
    img_bytes = preprocess_str(req.data)
    req_data = img_bytes.read()
    return predict(req_data)


@app.post("/predict/v2")
async def predict_file(image: UploadFile):
    req_data = await image.read()
    return predict(req_data)
