import json
import os

import aiohttp
import grpc
import requests

from src.inference import inference_pb2, inference_pb2_grpc

MODEL_SERVER = os.getenv("MODEL_SERVER", "http://localhost:8080")
MODEL_SERVER_GRPC = os.getenv("MODEL_SERVER_GRPC", "localhost:7070")
MODEL_NAME = os.getenv("MODEL_NAME", "drawclassifier")


def predict(req_data: bytes) -> dict:
    req = requests.post(f"{MODEL_SERVER}/predictions/drawclassifier", files={"data": req_data})
    if req.status_code == 200:
        return req.json()
    else:
        return {"error": req.status_code}


async def predict_async(req_data: bytes):
    async with aiohttp.ClientSession() as session:
        async with session.post(f"{MODEL_SERVER}/predictions/{MODEL_NAME}", data={"data": req_data}) as resp:
            if resp.status == 200:
                rs = await resp.text('utf-8')
                return json.loads(rs)
            else:
                return {"error": resp.status}


async def predict_grpc(req_data: bytes):
    async with grpc.aio.insecure_channel(MODEL_SERVER_GRPC) as channel:
        stub = inference_pb2_grpc.InferenceAPIsServiceStub(channel)
        response = await stub.Predictions(
            inference_pb2.PredictionsRequest(model_name=MODEL_NAME,
                                             input={'data': req_data}))

    try:
        prediction = response.prediction.decode('utf-8')
        return json.loads(prediction)
    except grpc.RpcError:
        return {"error": "GRPC Error"}
