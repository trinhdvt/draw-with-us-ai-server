from fastapi import status
from pydantic import BaseModel, validator

from app.exception import CustomException


class RequestModel(BaseModel):
    data: str

    @validator("data")
    def base64_img_check(cls, req_data: str):
        # request's type check
        support_type = ["image/jpeg", "image/png"]
        prefix = tuple(f"data:{_};base64," for _ in support_type)
        if not req_data.startswith(prefix):
            raise CustomException(message='Image type must be JPEG or PNG',
                                  status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)

        # return without base64 prefix
        image_data = req_data.split(',')[1]
        return image_data
