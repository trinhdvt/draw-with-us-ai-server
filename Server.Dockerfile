FROM python:3.9.12-slim-bullseye as production
MAINTAINER "trinhdvt"

WORKDIR /app

COPY server.requirements.txt requirements.txt

RUN python3 -m pip install --upgrade pip setuptools wheel --no-cache-dir \
    && pip3 install -r requirements.txt --upgrade --no-cache-dir

COPY . .
COPY deploy.env .env
ENV TZ=Asia/Ho_Chi_Minh

CMD ["gunicorn"]
