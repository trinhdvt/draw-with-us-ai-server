FROM python:3.9-slim-bullseye as production
MAINTAINER "trinhdvt"

ENV VIRTUAL_ENV=/home/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR /app

COPY server.requirements.txt requirements.txt

RUN python3 -m pip install -U setuptools --no-cache-dir \
    && pip3 install -r requirements.txt --upgrade --no-cache-dir

COPY . .
COPY deploy.env .env
ENV TZ=Asia/Ho_Chi_Minh

CMD ["gunicorn"]
