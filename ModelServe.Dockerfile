FROM python:3.9-slim-bullseye as production
MAINTAINER "trinhdvt"

ENV VIRTUAL_ENV=/home/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR /app

RUN apt update && apt autoremove -y \
    && apt install openjdk-11-jre-headless -y \
    && rm -rf /var/lib/apt/lists/* \
    && python3 -m pip install -U setuptools --no-cache-dir \
    && pip3 install torch torchvision --extra-index-url https://download.pytorch.org/whl/cpu --no-cache-dir \
    && pip3 install torchserve captum --no-cache-dir

COPY src/deployment/v2/model_store/draw_classifier.mar model-store/
COPY src/deployment/config.properties config.properties
EXPOSE 8080 8081 8082

CMD ["torchserve", "--start", "--ncs" , "--model-store", "model-store" , "--models" , "draw_classifier.mar", "--ts-config", "config.properties", "--foreground"]
