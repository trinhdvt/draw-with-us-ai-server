from base64 import b64decode
from io import BytesIO
from typing import Any

import requests
import os


def preprocess_str(img_data: str) -> BytesIO:
    img_bytes = BytesIO()
    img_bytes.write(b64decode(img_data))
    img_bytes.seek(0)
    return img_bytes


def predict(req_data: bytes) -> dict[str, Any]:
    MODEL_SERVER = os.getenv("MODEL_SERVER", "http://localhost:8080")

    req = requests.post(f"{MODEL_SERVER}/predictions/drawclassifier", files={"data": req_data})
    if req.status_code == 200:
        return req.json()
    else:
        return {"error": req.status_code}
