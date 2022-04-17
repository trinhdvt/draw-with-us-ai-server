from base64 import b64decode
from io import BytesIO


def preprocess_str(img_data: str) -> BytesIO:
    img_bytes = BytesIO()
    img_bytes.write(b64decode(img_data))
    img_bytes.seek(0)
    return img_bytes
